import streamlit as st

st.title("Uploading Video",anchor=False)
st.divider()

video_file = st.file_uploader("Upload video",['mp4','mov'])
button = st.button("click to upload")

if button:
    if video_file:
        st.video(video_file)
        st.success("Upload successfull")
    else:
        st.warning("upload error")