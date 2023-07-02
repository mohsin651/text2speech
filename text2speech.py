import streamlit as st
import pyttsx3

# Create a Streamlit app
st.title("Text to Speech")

# Text input
text = st.text_input("Enter text to be processed")

# Function to speak the entered text
def speak_text():
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Speak button
if st.button("Speak"):
    if not text:
        st.warning("Please enter text.")
    else:
        speak_text()
