# Built-In Tool: DuckDuckGoSearchRun ------------------------------------

from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

load_dotenv()

searchTool = DuckDuckGoSearchRun()

result = searchTool.invoke("Who won IPL 2025?")
print(result)
print(searchTool.name)
print(searchTool.description)
print(searchTool.args)


# Built-In Tool: Shell Tool ----------------------------------------
# pip install langchain-experimental

# from langchain_community.tools import ShellTool
# from dotenv import load_dotenv

# load_dotenv()

# searchTool = ShellTool()

# result = searchTool.invoke("Whoami")
# print(result)



# Built in Tools: 
# Many more tools available on LangChain