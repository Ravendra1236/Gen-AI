# # from langchain_openai import ChatOpenAI
# # from dotenv import load_dotenv
# # import streamlit as st

# # load_dotenv() 

# # st.header("Reasearch Tool")

# # userInput = st.text_input("Enter your prompt!")

# # model = ChatOpenAI(model = "gpt-4")

# # if st.button("Summarize"):
# #     result = model.invoke(userInput)
# #     st.write(result.content)

# ---------------------------------------------------------------------------------------
# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint 
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate
# load_dotenv() 

# st.header("Reasearch Tool")

# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# llm = HuggingFaceEndpoint(model="mistralai/Mistral-7B-Instruct-v0.3" )

# model = ChatHuggingFace(llm=llm)

# # Template : 
# template = PromptTemplate(
#     template="""
#     Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}

# Mathematical Details:

# Include relevant mathematical equations if present in the paper.

# Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# Analogies:

# Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['paper_input' , 'style_input' , 'length_input'],
# validate_template=True
# )

# prompt = template.invoke({
#     'paper_input' : paper_input,
#     "style_input" : style_input ,
#     "length_input" : length_input
# })

# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)


# ---------------------------------------------------------------------------------------
# After prompt Template Generator and loading JSON file here

# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint 
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate , load_prompt
# load_dotenv() 

# st.header("Reasearch Tool")

# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# llm = HuggingFaceEndpoint(model="mistralai/Mistral-7B-Instruct-v0.3" )

# model = ChatHuggingFace(llm=llm)

# # Template : 
# template = load_prompt("template.json")

# prompt = template.invoke({
#     'paper_input' : paper_input,
#     "style_input" : style_input ,
#     "length_input" : length_input
# })

# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.content)

# ---------------------------------------------------------------------------------------
# After Adding Chain here

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint 
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate , load_prompt
load_dotenv() 

st.header("Reasearch Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

llm = HuggingFaceEndpoint(model="mistralai/Mistral-7B-Instruct-v0.3" )

model = ChatHuggingFace(llm=llm)

# Template : 
template = load_prompt("template.json")


if st.button("Summarize"):
    chain = template | model 
    result = chain.invoke({
    'paper_input' : paper_input,
    "style_input" : style_input ,
    "length_input" : length_input
    })
    st.write(result.content)