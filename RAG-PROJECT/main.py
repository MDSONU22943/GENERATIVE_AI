from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader, TextLoader

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

data = TextLoader("RAG-PROJECT/document-loaders/notes.txt")
pdfdata = PyPDFLoader("RAG-PROJECT/document-loaders/GRU.pdf")

docs=data.load()
pdfdocs=pdfdata.load()

template=ChatPromptTemplate.from_messages([("system", "You are a helpful assistant and summarize the given text"),("human","{pdfdocs}")])

model = ChatMistralAI(model="mistral-small-2506")

prompt=template.format_messages(pdfdocs=pdfdocs[0].page_content)

result = model.invoke(prompt)
print(result.content)
