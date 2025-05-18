from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 

load_dotenv() 

# model = ChatOpenAI(model="gpt-4")         # Simple Accessing model
# model = ChatOpenAI(model="gpt-4" , temperature=1)         # Temprature parameter for creativity
model = ChatOpenAI(model="gpt-4" , temperature=1 , max_completion_tokens=10)        # restricting token

# result = model.invoke("What is the capital of India?")
# print(result) 

result = model.invoke("Write a poem on cricket.")
print(result.content) 
