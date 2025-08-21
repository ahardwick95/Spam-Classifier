import streamlit as st
def Intro():

    # This the first thing the user will see when they load up the application

    st.markdown("<h1 style='text-align: center;'>📧🚫 PhishDetective</h1>", unsafe_allow_html=True)

    st.markdown("""  Welcome to the PhishDetective application!""")
    st.markdown("This software uses features common in real-wolrd spam emails to assess whether a massgae is spam or beningn.")
        
    
    st.markdown("This application was tested with Naive Bayes and Logistic Regression.")
    st.markdown("The model being used for spam prediction is Logistic Regression as it performed the best.")
    st.markdown(" You can cycle through other pages in the application with the Navigation sidebar on the left. ")




    st.image("/Streamlit_App/pictures/Spam_Pic_1.png",use_container_width=True)

