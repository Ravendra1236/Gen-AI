from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough


load_dotenv()

# passThorugh = RunnablePassthrough()

# print(passThorugh.invoke({'name' : 'Ravendra'}))

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke - {text}",
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt , model , parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough() ,
    'explanation' : RunnableSequence(prompt2 , model , parser)
})

finalChain = RunnableSequence(joke_gen_chain , parallel_chain)

result = finalChain.invoke({'topic' : 'cricket'})
print(result)