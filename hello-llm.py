import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# NOTE: Enable once LMS server is up and model is loaded
# Use localhost because of network_mode: host
# local_llm = ChatOpenAI(
#     base_url=os.getenv("LM_STUDIO_URL"), 
#     api_key="not-needed",
#     model="granite-3b-code-instruct-128k"
# )

# NOTE: Enable once LMS server is up and model is loaded
# print("--- Testing Local Granite ---")
# try:
#     response = local_llm.invoke("Write a python script of hello-world")
#     print(response.content)
# except Exception as e:
#     print(f"Connection Error: {e}")

# Initialize OpenAI (uses OPENAI_API_KEY from .env)
model = ChatOpenAI(model="gpt-5-nano")

print("--- Testing GPT-5-nano ---")
try:
    # prompt = [HumanMessage("Write a python script of hello-world")]
    prompt = [HumanMessage("generate 5 page long text file for testing RAG")]
    response = model.invoke(prompt)
    print(response.content)
except Exception as e:
    print(f"Connection Error: {e}")


