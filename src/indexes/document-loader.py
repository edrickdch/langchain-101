from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("example_data/layout-parser-paper.pdf")
pages = loader.load_and_split()

print(f"Number of pages: {len(pages)}")
print(f"First document content: {pages[0]}")
