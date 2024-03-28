import streamlit as st 
from main import ask
with st.chat_message('assisstant'):
    st.write("Ask Any Ques About SKTHIVEL")

prompt=st.chat_input("Say something")
if prompt:
    st.chat_message("user").markdown(prompt)
    response=ask(prompt)
    st.chat_message("assistant").markdown(response)