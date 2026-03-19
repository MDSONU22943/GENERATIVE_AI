from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=200)


data=PyPDFLoader("RAG-PROJECT/document-loaders/GRU.pdf")
docs=data.load()
splits = splitter.split_documents(docs)
# print(splits)
# print(len(splits))
for i in splits:
    print(i.page_content)
