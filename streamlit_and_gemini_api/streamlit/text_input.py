import streamlit as st


st.title("My first streamlit web app!",anchor=False)

st.header("Content1",anchor=False, divider=True)
st.subheader("content1 sub header")
st.text("Hello from streamlit!")
st.markdown("**Hello** from *streamlit*")

a = 10
b= 20
st.write(a ,b)