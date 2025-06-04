from langchain_community.document_loaders import PyPDFLoader

# Loader object:
loader = PyPDFLoader('cpp_quesBank.pdf' )

# Loading that document:
docs = loader.load()

print(docs)
# print(docs[0].page_content)  # Page1
# print(len(docs))                # Total no. of pages


