# # ToolBinding
# from langchain_core.tools import tool
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()

# @tool 
# def multiply(a:int , b:int)->int:
#     """Multiply the 2 numbers and return their product."""
#     return a*b

# # result = multiply.invoke({"a":4 , "b":10})
# # print(result)

# # Take Model
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# # Bind Tool with Model
# llm_with_tool = llm.bind_tools([multiply])

# # print(llm_with_tool)

# # Tool Calling: Dont execute , it just advice tool with parameters and which tool to call
# result = llm_with_tool.invoke("Can you multiply 2 and 5")
# # print(result) # Will call tool
# # print(result.tool_calls)

# # Tool Execution: 
# result1 = multiply.invoke(result.tool_calls[0])
# print(result1)


# Organising better with messages:
# ToolBinding
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , AIMessage
from dotenv import load_dotenv
load_dotenv()


# Will maitain chat history
query = HumanMessage("What is the result of multplication of 2 and 5")

message = [query]

@tool 
def multiply(a:int , b:int)->int:
    """Multiply the 2 numbers and return their product."""
    return a*b


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

llm_with_tool = llm.bind_tools([multiply])

result = llm_with_tool.invoke(message)     # Return AI message

message.append(result)

tool_result = multiply.invoke(result.tool_calls[0]) # return tool message

message.append(tool_result) 

finalResult = llm_with_tool.invoke(message)
print(finalResult.content)

# It's like talking to an assistant:

# You: "Multiply 2 and 5."

# Assistant: "Okay, calling the multiply tool..."

# (You show the result: 10)

# Assistant: "Got it. Now, what next?"

# Without the "history," the assistant would forget what was said or done before.


