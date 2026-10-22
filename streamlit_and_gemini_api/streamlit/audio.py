import streamlit as st 

st.title("Uploading Audio/Video", anchor=False)

st.divider()

# audio from local address 
st.audio('aduio/loka_music-inspiring-travel-acoustic-621191.mp3')

# audio from upload
st.divider()
file = st.file_uploader("Upload audio",['mp3'])
if file:
    st.audio(file)