# ToolBinding
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

@tool 
def multiply(a:int , b:int)->int:
    """Multiply the 2 numbers and return their product."""
    return a*b

# Take Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# Bind Tool with Model
llm_with_tool = llm.bind_tools([multiply])


result = llm_with_tool.invoke("Can you multiply 2 and 5")
# print(result)

# Here we are calling our Tool 
# result1 = multiply.invoke(result.tool_calls[0]['args'])
# print(result1)

# But we can also get Tool message and maintain a chat history
result2 = multiply.invoke(result.tool_calls[0]) 
# This return tool_message
print(result2)