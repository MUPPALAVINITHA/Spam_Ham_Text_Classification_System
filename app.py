import streamlit as st
import pickle

try:
    model = pickle.load(open("model.pkl", "rb"))
except Exception as e:
    st.error(f"Model loading error: {e}")

st.title("Spam Classifier")

text = st.text_area("Enter message", placeholder="Type your message here...")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter a message")
    else:
        pred = model.predict([text])[0]

        if pred == 1:
            st.error("Spam")
        else:
            st.success("Ham")