# Due to a bug in litellm, we need to force UTF-8 encoding
# Set the environment variable and restart the script
# This MUST be done prior to importing dspy!
import os
import sys
if os.environ.get("PYTHONUTF8") != "1":
    os.environ["PYTHONUTF8"] = "1"
    os.execv(sys.executable, [sys.executable] + sys.argv)

import dspy

lm = dspy.LM('ollama/gemma3:1b', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)

output = lm("Say this is a test!", temperature=0.7) # => ['This is a test!']
print(output)
output = lm(messages=[{"role": "user", "content": "Say this is a test!"}]) # => ['This is a test!']
print(output)
