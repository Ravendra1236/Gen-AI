from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# prompt(input) -> model -> Report -> model -> Summary(output)

# Step1 : prompt 1 (Report)
prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic'] 
)

# Step2 : prompt 2 (Summary)

prompt2 = PromptTemplate(
    template="Generate a 5 points summary on following text \n {text}",
    input_variables=['text']
)

# Step3 : model 
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Step4 : parser
parser = StrOutputParser() 

chain = prompt1 | model | parser | prompt2 | model | parser 

result = chain.invoke({'topic' : 'React in future world.'})
print(result)
# chain.get_graph().print_ascii()

# In LangChain, when you use the | (pipe) operator to build a chain, the output of one component automatically becomes the input of the next. So in your code:

# chain = prompt1 | model | parser | prompt2 | model | parser 
# Here’s how LangChain automatically handles the flow:

# prompt1 takes {"topic": "React in future world"} and outputs a formatted string like:
# "Generate a detailed report on React in future world."

# model takes that string and generates a detailed report.

# parser extracts the plain text output of the model (the report string).

# That report text is now automatically passed as input to prompt2, which expects a variable {text}.

# 🟢 This is the key part:
# Since the output of the previous parser is a plain string, LangChain automatically maps it to {text} in prompt2 — because prompt2 has only one input variable (text).

# This smart auto-mapping is handled by LangChain’s internal logic when chaining.

# Then the same model and parser steps are applied again to generate and return the summary.