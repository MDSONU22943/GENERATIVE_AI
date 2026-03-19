from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)

data=TextLoader("RAG-PROJECT/document-loaders/notes.txt")

docs=data.load()

splits = splitter.split_documents(docs)
# print(splits)
# print(len(splits))
for i in splits:
    print("********")
    print(i.page_content)
    print("-----------")