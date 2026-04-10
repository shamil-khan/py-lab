import os
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-5-nano")

# completion = model.invoke('Hi there!') 
# # Hi!

# completions = model.batch(['Hi there!', 'Bye!'])
# # ['Hi!', 'See you!']

for token in model.stream('Bye!'):
    print(token)
    # Good
    # bye
    # !