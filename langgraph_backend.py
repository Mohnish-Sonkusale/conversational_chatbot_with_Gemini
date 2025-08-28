
from langgraph.graph import END, START, StateGraph
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import sqlite3

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    print("Sucessfully Load GOOGLE_API_KEY")
else:
    print("API key not found in .env file.")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

connection = sqlite3.connect(database = "chatbot.db", check_same_thread=False)

checkpointer = SqliteSaver(conn = connection)

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_thread_numer():
    total_thread = set()
    threads = checkpointer.list(None)
    for thread in threads:
        total_thread.add(thread.config["configurable"]["thread_id"])
    return list(total_thread)

