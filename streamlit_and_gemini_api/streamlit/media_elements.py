import streamlit as st

st.title("Input files",anchor=False)
st.divider()

# file_uploader 
images = st.file_uploader("Upload Image",type=['jpg','jpeg','png'], accept_multiple_files=True)

# if image:
#     st.image(image)

if images:
    cols = st.columns(len(images))
    
    for i, img in enumerate(images):
        with cols[i]:
            st.image(img)