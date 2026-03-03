from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("groq:llama-3.1-8b-instant")

# print(model)
response = model.invoke("what is GEnAI?")

print(response.content)
