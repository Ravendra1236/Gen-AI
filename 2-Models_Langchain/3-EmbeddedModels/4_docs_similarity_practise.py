from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv() 

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2" )

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


query = "Tell me about Sachin Tendulkar."

embedding_docs = embedding.embed_documents(documents)
embedding_query = embedding.embed_query(query) 

# cosine_similarity : Both values must be 2D list
print(cosine_similarity([embedding_query] , embedding_docs))

# 2D to 1D list
scores = cosine_similarity([embedding_query] , embedding_docs)[0]
# print(scores)

# Just like mapping : Attaching indices
# print(list(enumerate(scores)))

# Asc Order sorted and max value will got at last so we will access from there.
index , score = sorted(list(enumerate(scores)), key=lambda x : x[1])[-1]

# print(index) 
print(query)
print(documents[index])
print("Similarity Score: " , score)





