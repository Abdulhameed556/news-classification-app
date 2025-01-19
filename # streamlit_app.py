# streamlit_app.py

import streamlit as st
import joblib
import re

# Load the trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("count_vectorizer_for_fake_news_model.pkl")

# Function to preprocess user input
def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

# Streamlit app
def main():
    st.title("Fake News Detector")
    st.write("Classifies news articles as Fake or Real.")
    
    #Input from user
    title = st,text_input("News Title")
    content = st.text_area("News Content")
    
    if st.button("Classify"):
        # Preprocess and combine inputs
        full_text = f"{title} {content}"
        cleaned_text = clean_text(full_text)
        
        # Transform input using vectorizer
        input_vectorized = vectorizer.transform([cleaned_text])
        
        # predict label
        prediction = model.predict(input_vectorized)
        result = "REAL" if prediction[0] == 1 else "FAKE"
        
        # Display result 
        st.subheader(f"The news is classified as: {result}")
        
if __name__ == "__main__":
    main()        
