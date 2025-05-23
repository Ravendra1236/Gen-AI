from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() 

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash" , max_tokens=10)

result = model.invoke("Capital of India?")
print(result.content)