from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()



# BeautifulSoup extracts the text present in HTML page

url = "https://www.flipkart.com/samsung-galaxy-a56-5g-awesome-graphite-256-gb/p/itm33a726cc39ea5"

loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)

# Task : 
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n{text}",
    input_variables=['question','text']
)

chain = prompt | model | parser  

result = chain.invoke({'question': "What is the price of this product?" , 'text' : docs[0].page_content})
print(result)