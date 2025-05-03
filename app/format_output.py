import dspy
from lm import lm

class FormatAsMarkdown(dspy.Signature):
    """
    You are a markdown and json expert. Always:
    - Read the entire input carefully
    - Write markdown based solely on the input
    - Return a markdown formatted string
    - Break the result into sections based on the json input
    - Be concise, and disregard any null or empty values in the input json
    """
    json_object: str = dspy.InputField()
    markdown: str = dspy.OutputField(desc="A markdown string that is a human readable article.")


class FormatOutputModule(dspy.Module):
    def __init__(self):
        super().__init__()

        # Configure dspy
        dspy.configure(lm=lm)

        # Add each extractor signature
        self.markdown_formatter = dspy.ChainOfThought(signature=FormatAsMarkdown)


    def format_as_markdown(self, *, text: str) -> str:
        # Get the output string as markdown
        result = self.markdown_formatter(json_object=text).markdown

        return result
