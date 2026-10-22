import streamlit as st


st.title("Taking input in streamlit",anchor=False)
st.divider()

name = st.text_input("Enter your name: ",placeholder="Type your name ...")
# print(type(name))

# st.write("You typed : ",name)

st.divider()

age = st.number_input("Enter your age :",value=None,placeholder="Type your age ...")

# st.write("You typed :",age)

# st.divider()

# password = st.text_input("Enter your Password :", type="password")
# st.write("you typed :",password)

# button
clicked = st.button("Confirm",type="primary")

if clicked:
    st.write(f"Your name is {name} and You are {age} years old.")
    
    
st.divider()

options = st.selectbox("Choose your tech stack: ", ("nextJ","Java","SpringBoot"), index=None, accept_new_options=True)

st.write(options)
