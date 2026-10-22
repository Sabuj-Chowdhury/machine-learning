from google import genai
import os
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
     model="gemini-3.8-flash",
    input="Give me idea of gemni api integreation in python project within 100 words."
)
st.markdown(interaction.output_text)