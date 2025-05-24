from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# prompt(input) -> model -> Output(string) 

# Step1 : prompt
prompt = PromptTemplate(
    template="Generate 5 small intersting points about {topic}",
    input_variables=['topic'] 
)

# Step2 : model 
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash" , max_tokens=100)


# Step3 : output(string)
parser = StrOutputParser()

# Simple Chain: 
chain = prompt | model | parser    

result = chain.invoke({'topic' : 'cricket'})

print(result)

# chain.get_graph().print_ascii()
