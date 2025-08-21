import streamlit as st

def Upgrades():
    # This outlines the future upgrades to the application that can help improve performance

    st.markdown("<h1 style='text-align: center;'> PhishDetective Upgrades</h1>", unsafe_allow_html=True)

    st.markdown("""The original features developed for this application were based on the frequency of certain artifacts
                such as special characters or URLs.""" )
    st.markdown("""Well these are signficant for differentiation, they are not enough to fully help classify spam messages. """)
    st.markdown("""As such the following are future upgrades that could help improve performance of the application: """)
    st.markdown(" ")
    st.markdown("""1. TF-IDF helps assert importance or weight to words better than CountVectorizer. """)
    st.markdown("""2. N-gram ( other unigram) analysis helps derive context and with Collocations, derive statistical signficance to the n-grams """)
    st.markdown("""3. Type-Token Ratio to examine repetitve words. """)
    st.markdown("""4. Examine Readability metrics, since spam can sometimes be incomprehensible.  """)
    
    
    
    




    
