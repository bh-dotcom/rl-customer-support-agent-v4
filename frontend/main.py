import streamlit as st
import requests

st.title("RL Customer Support Agent")

query = st.text_input("Enter your query:")

if st.button("Send"):
    response = requests.post("http://127.0.0.1:8000/step", json={"query": query})
    st.write("Agent Reply:", response.json()["observation"]["state_text"])

def main():
    st.write("Frontend running")

if __name__ == "__main__":
    main()
