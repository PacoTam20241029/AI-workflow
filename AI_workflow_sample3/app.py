import streamlit as st
from llm import answer

# Streamlit app
st.title("System Design Workflow Generator")

# Create a text input box
text_input = st.text_input("Input your system design requirements")

# Create a submit button
if st.button("Submit"):
    user_prompt = text_input
    system_prompt = "Generate a system design workflow based on the following requirements:"
    result = answer(system_prompt, user_prompt)
    st.markdown("## Response")
    st.write(result)