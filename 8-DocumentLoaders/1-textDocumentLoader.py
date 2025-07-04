from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n{poem}",
    input_variables=['poem']
)

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()

# Consists of list in which 0th documents is ours which contains page_content and metadata

print(docs)
# print(type(docs))
# print(len(docs)
# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser 

result = chain.invoke({'poem' : docs[0].page_content})
# print(result)

