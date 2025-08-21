import streamlit as st
import pandas as pd
from F2_Intro import Intro
from F3_Predictor import Spam_Predictor
from F4_Spam_Features import Spam_Features_Display
from F5_Model_Comparisons import Model_Comparisons
from F6_GenAI_SMS_Testing import Gen_AI_Model_Comparisons
from F7_Future_Upgrades import Upgrades

st.set_page_config(page_title="PhishDetective",layout="wide")

st.sidebar.title("📨 Navigation")
selected_page = st.sidebar.selectbox("Choose a page:", ["About", "Spam Predictor","Spam Features","Model Comparisons","GenAI Testing","Future Upgrades"])

if selected_page == "About":
    Intro()
elif selected_page == "Spam Predictor":
    Spam_Predictor()
elif selected_page == "Spam Features":
    Spam_Features_Display()
elif selected_page == "Model Comparisons":
    Model_Comparisons()
elif selected_page == "GenAI Testing":
    Gen_AI_Model_Comparisons()
elif selected_page == "Future Upgrades":
    Upgrades()

    
