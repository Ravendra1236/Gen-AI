from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chatHistory'),
    ('human','{query}')
])

chatHistory = []
# load chat history
with open('chatHistory.txt') as f:
    chatHistory.extend(f.readlines())

print(chatHistory)

# create prompt
prompt = chat_template.invoke({'chatHistory':chatHistory, 'query':'Where is my refund'})

print(prompt)