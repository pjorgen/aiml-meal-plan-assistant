import dspy

lm = dspy.LM(
    model='ollama/gemma3:4b',
    api_base='http://localhost:11434',
    api_key='',
    cache=False
)
