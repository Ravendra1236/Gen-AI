from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableBranch , RunnablePassthrough


load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Summarize the following text \n {text}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

reportGenChain = RunnableSequence(prompt1 , model , parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split())>500 , RunnableSequence(prompt2 , model , parser)),
    
    RunnablePassthrough()
)

finalChain = RunnableSequence(reportGenChain , branch_chain)

result = finalChain.invoke({'topic' : 'Russia vs USA'})


print(result) 
