from langchain_cohere import ChatCohere
from langchain.schema.messages import HumanMessage, SystemMessage
import os

chat = ChatCohere(cohere_api_key="rOaoDS76oLju9iDM04XOlC5lEPCbqP2o0WcD5QrU")
messages = [
    SystemMessage(content="You are iron man"),
    HumanMessage(content="Tell me a That's what she said joke")
]

response = chat.invoke(messages)
print(response.content)