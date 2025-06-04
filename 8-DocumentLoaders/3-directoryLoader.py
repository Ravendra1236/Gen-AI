from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader

loader = DirectoryLoader(
    path='docs' ,
    glob='*.pdf' ,
    loader_cls=PyPDFLoader
)
# Load : Time consuming
# docs = loader.load()

# Lazy_load : Lots of docs
docs = loader.lazy_load()



# Total pages of all pdf
# print(len(docs))

# Last Page: 
# print(docs[0].page_content)
# print(docs[26].page_content)

# Problem:
# Loading time is very much 
# If there were 100 pdf to put on memory then also it was difficult 
# That is why we use lazy_loading

for doc in docs:
    print(doc.metadata)
    
