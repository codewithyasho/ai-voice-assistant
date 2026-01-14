from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:deepseek-v3.1:671b-cloud")


with open("human-text.txt", "r", encoding="utf-8") as f:
    query = f.read()

response = model.invoke(query)
result = response.content

with open("llm-text.txt", "w", encoding="utf-8") as f:
    f.write(result)
