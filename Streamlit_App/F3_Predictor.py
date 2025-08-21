import streamlit as st
from joblib import load
from Streamlit_App/Scripts/Spam_Preprocessor import Message_Preprocessor

def Spam_Predictor():

    st.markdown("<h1 style='text-align: center;'>Spam Predictor!</h1>", unsafe_allow_html=True)

    # loads the logistic regression model and vectorizer to help transform message
    LogReg = load('Streamlit_App/Models/LogReg_Model.joblib')
    vectorizer = load("Streamlit_App/Models/Vectorizer.joblib")

    # where the user can enter their message
    message = st.text_area("Enter a message:")

    if st.button("Predict"):
        if message.strip():  # check if not empty
            Preprocessed_Message = Message_Preprocessor(message) # preprocess the message
            Prediction = LogReg.predict(Preprocessed_Message)[0] # pass it to the model and collect prediction

            if Prediction == 1:
                st.error("🚨 This looks like **SPAM**!")
            else:
                st.success("✅ This looks **Safe (Ham)**!")
        
    else:
        st.warning("Please enter a message to analyze")


        

