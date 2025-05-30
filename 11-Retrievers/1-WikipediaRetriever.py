from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2 , lang='en')

query = "The geopolitical history of india and pakistan from the perspective of a chinese."

docs = retriever.invoke(query)


# Print retrieved content
for i , doc in enumerate(docs):
    print(f"\n--Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...") #truncate for display