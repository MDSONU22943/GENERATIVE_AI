from langchain_community.document_loaders import TextLoader

data=TextLoader("RAG-PROJECT/document-loaders/notes.txt")

docs=data.load()
# print(docs)
# print(len(docs))
print(docs[0].page_content)