# With OpenAI

# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv 
# from typing import TypedDict

# load_dotenv() 


# model = ChatOpenAI(model='gpt-4')

# class Review(TypedDict):
#     summary : str 
#     sentiment : str 

# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful
                                 
# Review by Nitish Singh
# """)

# print(result)

# Annotated __________________________________________________________________________________

# from langchain_openai import ChatOpenAI 
# from dotenv import load_dotenv 
# from typing import TypedDict , Annotated

# load_dotenv() 

# model = ChatOpenAI(model='gpt-4')

# # Schema + Description : 

# class Review(TypedDict):
#     summary : Annotated[str , 'A brief summary of the review']
#     sentiment : Annotated[str , 'return sentiment of the review either in positive , negative or neutral']

# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke("""


# I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

# The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

# However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

# Pros:
# Insanely powerful processor (great for gaming and productivity)
# Stunning 200MP camera with incredible zoom capabilities
# Long battery life with fast charging
# S-Pen support is unique and useful

# Review by Nitish Singh
# """)

# print(result)


# typedDict + Annotation + More features : 

from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
from typing import TypedDict , Annotated , Optional , Literal

load_dotenv() 

model = ChatOpenAI(model='gpt-4')

# Schema + Description : 

class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""


I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Review by Nitish Singh
""")

print(result)




# Problem with typedDict : 
# Only for representation not data validation 
# May be our LLM give int instead of str
# so thats why we use pydantic for data validation


# Why typedDict is not applying for gemini 
# 🔍 Reason: TypedDict is a static typing tool, not a runtime validator
# TypedDict (from Python's typing module) is used only for type hints—it's not a real class with methods or structure at runtime.

# So when LangChain or any structured output parser tries to:

# Validate

# Instantiate

# Enforce schema

# Parse values into objects

# …it cannot use TypedDict because it doesn't exist at runtime as a schema object. It's just metadata for editors and linters (e.g., for mypy, Pyright).

