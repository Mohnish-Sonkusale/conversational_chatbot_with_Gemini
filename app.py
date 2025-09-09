import streamlit as st
from langgraph_backend import chatbot, retrieve_thread_numer
from langchain_core.messages import HumanMessage
import uuid

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id "] = thread_id
    add_thread(st.session_state["thread_id "])
    st.session_state["messsage_history"] = []

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_thread"].append(thread_id)

def load_coversation():
    return chatbot.get_state(config={"configurable": {"thread_id" : thread_id}}).values["message"]
    
#########################   Session Setup  #######################
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_thread" not in st.session_state:
    st.session_state["chat_thread"] = retrieve_thread_numer()

add_thread(st.session_state["thread_id"])

########################  SideBar UI ############################

st.sidebar.title("LANGGRAPH CHATBOT")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("MY CONVERSATIONS")

for thread_id in st.session_state["thred_id"][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state["thread_id"] = thread_id
        messages = load_coversation(thread_id)
        temp_message = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = "User"
            else:
                role = "Assistance"
            temp_message.append({"role": role, "content":msg.content})

        st.session_state["message_history"] = temp_message
