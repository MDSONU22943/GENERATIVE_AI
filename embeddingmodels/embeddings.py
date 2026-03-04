from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
texts=["Hello, how are you?", "Hello, how are you?", "Hello, how are you?"]

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=64)
vector = embeddings.embed_documents(texts)
# vector = embeddings.embed_query("Hello, how are you?")


print(vector)