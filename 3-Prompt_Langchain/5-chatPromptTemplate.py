# Making prompt template for dynamic chatbotsf 

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
    ('system' ," You are a helpful {domain} expert"),
    ('human' , "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({"domain" : "cricket" , "topic":"wicket"})

print(prompt)