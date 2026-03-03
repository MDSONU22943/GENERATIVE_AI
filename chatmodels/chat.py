from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# print(model)
response = model.invoke("Why do parrots talk?")

print(response.content)
