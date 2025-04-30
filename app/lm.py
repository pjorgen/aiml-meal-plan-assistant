import dspy

lm = dspy.LM(
    model='ollama/gemma3:1b',
    api_base='http://localhost:11434',
    api_key=''
)
