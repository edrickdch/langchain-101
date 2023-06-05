from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
text = "This is a test."
query_result = embeddings.embed_query(text)

print(f"Number of dimensions: {len(query_result)}")
print(f"[{query_result[0]}, {query_result[1]}, ...]")


