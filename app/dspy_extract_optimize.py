import pathlib

import dspy
from dspy_data import train_set, dev_set
from extract_info import ExtractInfoModule

def information_extraction_metric(gold, pred, trace=None):
    score = 0
    if gold.meal_count == pred.meal_count: score += 1
    if gold.people_per_meal == pred.people_per_meal: score += 1
    if gold.diet_restrictions == pred.diet_restrictions: score += 1
    if gold.nutrition_targets == pred.nutrition_targets: score += 1
    if gold.cuisine_likes == pred.cuisine_likes: score += 1
    if gold.cuisine_dislikes == pred.cuisine_dislikes: score += 1
    if gold.food_likes == pred.food_likes: score += 1
    if gold.food_dislikes == pred.food_dislikes: score += 1
    if trace is not None: return score >= 8
    return score / 8 # Normalize to 0.0-1.0

student = ExtractInfoModule()

optimizer = dspy.BootstrapFewShot(
    metric=information_extraction_metric,
    metric_threshold=0.75,
    max_labeled_demos=32,
    max_bootstrapped_demos=8,
    max_rounds=5,
    max_errors=30
)

optimized_program = optimizer.compile(student=student, trainset=train_set)


# For reference, evaluate a set of test data and output the scores
def test_unoptimized():
    scores = []
    for example in dev_set:
        response = student.forward(text=example.text)
        score = information_extraction_metric(example, response)
        scores.append(score)
    print("Cumulative score for unoptimized module: ", scores)


def test_optimized():
    scores = []
    for example in dev_set:
        response = optimized_program(text=example.text)
        score = information_extraction_metric(example, response)
        scores.append(score)
    print("Cumulative score for optimized module: ", scores)

# Run the tests
test_unoptimized()
test_optimized()

# Export the optimized model
path = pathlib.Path("optimized", "extract_optimized.json")
optimized_program.save(str(path))


# Last scores: unoptimized (2), optimized (2.25) -> cumulative, not averaged