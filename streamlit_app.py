import streamlit as st

st.set_page_config(page_title="RAG Chatbot")

st.title("📚 RAG Chatbot")
st.write("Welcome Mayuri 👋")

question = st.text_input("Ask a question:")

if question:
    st.write("You asked:", question)
