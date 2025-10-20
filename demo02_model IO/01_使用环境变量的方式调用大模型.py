import os

from langchain_openai import ChatOpenAI

print(os.environ["OPENAI_BASE_URL"])
print(os.environ["OPENAI_API_KEY1"])

# 1、调用对话式模型
chat_model = ChatOpenAI(
    # 必须要设置的3个参数
    model="gpt-4o-mini",
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"]
)

# 2、调用模型
response = chat_model.invoke("什么是langchain?")

# 3、查看相应文本
print(response.content)
