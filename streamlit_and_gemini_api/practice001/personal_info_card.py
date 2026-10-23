import streamlit as st 

st.title("Personal Info Card App",anchor=False)
st.divider()

# name
name = st.text_input("Name :",placeholder="Enter your name...")
# age
age = st.number_input("Age :",value=None,placeholder="Enter your age...")
# profession
profession = st.selectbox("Choose profession :",("Student", "Employee", "Businessman", "Freelancer"), index=None )

st.divider()

isClicked = st.button("Confirm",type="primary")

if isClicked:
    st.success("All information was provided")
    st.write(f"your name is : {name}")
    st.write(f"your age is : {age}")
    st.write(f"You are {profession}")