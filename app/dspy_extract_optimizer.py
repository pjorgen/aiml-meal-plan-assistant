import json
import pathlib
from difflib import SequenceMatcher
import dspy
from pydantic import BaseModel
from dspy_data import train_set, dev_set
from extract_info import ExtractInfoModule

class TestResult(BaseModel):
    prompt: str
    score: float
    expected: dict
    predicted: dict

test_results = []
save_results = True

def information_extraction_metric(gold, pred, trace=None):
    score = 0
    if gold.output["meal_count"] == pred.meal_count: score += 1
    if gold.output["people_per_meal"] == pred.people_per_meal: score += 1
    score += SequenceMatcher(None, gold.output["meal_types"], pred.meal_types).ratio()
    score += SequenceMatcher(None, gold.output["include_cuisines"], pred.include_cuisines).ratio()
    score += SequenceMatcher(None, gold.output["exclude_cuisines"], pred.exclude_cuisines).ratio()
    score += SequenceMatcher(None, gold.output["diets"], pred.diets).ratio()
    score += SequenceMatcher(None, gold.output["intolerances"], pred.intolerances).ratio()
    score += SequenceMatcher(None, gold.output["include_ingredients"], pred.include_ingredients).ratio()
    score += SequenceMatcher(None, gold.output["exclude_ingredients"], pred.exclude_ingredients).ratio()
    if gold.output["high_fiber"] == pred.high_fiber: score += 1
    if gold.output["high_protein"] == pred.high_protein: score += 1
    if gold.output["low_calorie"] == pred.low_calorie: score += 1
    if gold.output["low_carb"] == pred.low_carb: score += 1
    if gold.output["low_fat"] == pred.low_fat: score += 1
    if gold.output["low_cholesterol"] == pred.low_cholesterol: score += 1
    if gold.output["low_sat_fat"] == pred.low_sat_fat: score += 1
    if gold.output["low_sodium"] == pred.low_sodium: score += 1

    # Save test out to test result
    if save_results:
        test_result = TestResult(
            prompt = gold.prompt,
            score = score / 17,
            expected = gold.output,
            predicted = pred.model_dump()
        )
        test_results.append(test_result)

    if trace is not None:
        return score >= 17
    else:
        return score / 17 # Normalize to 0.0-1.0

student = ExtractInfoModule()

bootstrap_optimizer = dspy.BootstrapFewShot(
    metric=information_extraction_metric,
    metric_threshold=0.75,
    max_labeled_demos=16,
    max_bootstrapped_demos=4,
    max_rounds=5,
    max_errors=30
)

optimized_program = bootstrap_optimizer.compile(student=student, trainset=train_set)

# For reference, evaluate a set of test data and output the scores
def test_unoptimized():
    scores = []
    for example in dev_set:
        response = student.extract_meal_criteria(text=example.text)
        score = information_extraction_metric(example, response)
        scores.append(score)
    print("Scores for unoptimized module: ", scores)
    print("Cumulative score for unoptimized module: ", sum(scores))


def test_optimized():
    scores = []
    for example in dev_set:
        response = optimized_program(text=example.text)
        score = information_extraction_metric(example, response)
        scores.append(score)
    print("Scores for optimized module: ", scores)
    print("Cumulative score for optimized module: ", sum(scores))

# Run the tests
test_unoptimized()
test_optimized()

# Export the optimized model
path = pathlib.Path("optimized", "extract_optimized.json")
optimized_program.save(str(path))

# Export the test results for review
if save_results:
    path = pathlib.Path("optimized", "test_results.json")
    with open(path, "w") as f:
        json.dump([r.model_dump() for r in test_results], f, indent=4)

# BootstrapFewShot scores: optimized (2.647) -> cumulative, not averaged
