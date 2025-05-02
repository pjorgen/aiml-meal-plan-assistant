import dspy
from lm import lm
from pathlib import Path

class FormatAsMarkdown(dspy.Signature):
    """Given a structured JSON object, write a markdown formatted article for better readability."""
    json_object: str = dspy.InputField()
    markdown: str = dspy.OutputField(desc="A markdown string that is a human readable article.")


class FormatOutputModule(dspy.Module):
    def __init__(self):
        super().__init__()

        # Configure dspy
        dspy.configure(lm=lm)

        # Load optimized module from file
        #path = Path("optimized", "extract_optimized.json")
        #self.load(str(path))

        # Add each extractor signature
        self.markdown_formatter = dspy.ChainOfThought(signature=FormatAsMarkdown)


    def format_as_markdown(self, *, text: str) -> str:
        # Get the output string as markdown
        result = self.markdown_formatter(json_object=text).markdown

        return result
