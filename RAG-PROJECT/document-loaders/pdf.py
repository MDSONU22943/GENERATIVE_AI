from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("RAG-PROJECT/document-loaders/GRU.pdf")
docs=data.load()
# print(docs)
# print(len(docs))

print(docs[14])