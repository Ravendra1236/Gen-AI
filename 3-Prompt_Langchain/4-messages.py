from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(model="mistralai/Mistral-7B-Instruct-v0.3" , max_new_tokens=10)

model = ChatHuggingFace(llm=llm)



messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about langchain")
]

result= model.invoke(messages) 

messages.append(AIMessage(content=result.content))

print(result.content.strip())

print(messages)
