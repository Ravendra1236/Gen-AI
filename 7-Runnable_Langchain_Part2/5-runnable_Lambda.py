from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableParallel , RunnableLambda , RunnableSequence
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


def wordCount(prompt):
    return len(prompt.split())

runnbaleCount = RunnableLambda(wordCount)

print(runnbaleCount.invoke("Hello My Name is Ravendra"))
