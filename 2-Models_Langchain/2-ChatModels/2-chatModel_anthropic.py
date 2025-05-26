from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv 

load_dotenv() 

model = ChatAnthropic(model="claude-3-5-sonnet-20241022")
# Similar here we can set temperature and max token

result = model.invoke("Write poem on cricket")

print(result.content)