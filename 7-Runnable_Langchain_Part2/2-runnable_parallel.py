from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel


load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a concise tweet about {topic} in plain text format",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a professional LinkedIn post about {topic} in plain text format",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1 , model , parser) ,
    'linkedin' : RunnableSequence(prompt2 , model , parser)
})

# result = parallel_chain.invoke({'topic' : "AI"})

# print(result)

prompt3 = PromptTemplate(
    template="""Combine these posts into a formatted output:

Tweet:
{tweet}

LinkedIn Post:
{linkedin}""",
    input_variables=['tweet', 'linkedin']
)

finalChain = RunnableSequence(parallel_chain , prompt3 , model , parser)

result = finalChain.invoke({'topic' : "AI"})

print(result)