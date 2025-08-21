import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

def Spam_Features_Display():

    st.markdown("<h1 style='text-align: center;'>Spam Features</h1>", unsafe_allow_html=True)
    st.markdonw("In this section we explore several features present in spam and compare them to ham messages.")

    Spam_df = pd.read_csv('Streamlit_App/Data/02_Spam_EDA_Phase.csv')
    count = Spam_df['Result'].value_counts()


    categories=['Ham','Spam'] # used to help  make the x axis for bar charts

    # boolean masking for dataset to separate spam from ham for easier processing
    Spam_bool_marker = Spam_df['Result'] == 'spam'
    Non_Spam_bool_marker = Spam_df['Result'] == 'ham'

    Spam_Messages = Spam_df[Spam_bool_marker]
    Ham_Messages = Spam_df[Non_Spam_bool_marker]

    Num_Ham_Spam = len(Ham_Messages)
    Num_Spam = len(Spam_Messages)

    #Each choice beside choice calcuates the average presence of that specific feature in spam and ham
    # for instance, in character length, the bar chart displays 
    # the average character length of all the spam messages and then ham messages and compares them
    
    with st.expander("📊 Review Chart Explanations"):
    # Dropdown to pick which chart explanation to show
        choice = st.selectbox("Select a chart to review explanation:", 
                          ["Figure 1 : Class Imbalance","Figure 2 : Character Length", 
                           "Figure 3 : Word Length", "Figure 4 : Special Character Count","Figure 5 : Number of Digits","Figure 6 : Uppercase Word Count", 
                           "Figure 7 : URL Count", "Figure 8 : Email address Count","Figure 9 : Suspcious Word Count"])

    # Show explanation based on choice
        if choice == "Figure 1 : Class Imbalance":

            st.write("""Based on the graph, we can see that the distribution of spam messages 
                 is significantly lower in comparsion to that of ham (benign) messages.""")
            
            Amount=[count['ham'],count['spam']]
            


            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y=Amount, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Spam vs Non-Spam class count")
            st.pyplot(fig)
            
        
        elif choice == "Figure 2 : Character Length":

            st.write(""" There are usually more characters in spam than ham messages as they tend to be more wordy overall.""")

            Num_Spam = len(Spam_Messages)
            Ave_Spam_Mes_Len = Spam_Messages['num_chars'].sum() / Num_Spam

            Num_Ham_Spam = len(Ham_Messages)
            Ave_Ham_Mes_Len = Ham_Messages['num_chars'].sum() / Num_Ham_Spam
            
            Y = [Ave_Ham_Mes_Len,Ave_Spam_Mes_Len]
    
            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average character count, Spam vs Ham")
            st.pyplot(fig)
            
    
        elif choice == "Figure 3 : Word Length":
            st.write("""As established in the character length analysis, spam tends to have a lot more words than ham messages. 
                     This is proabably due to most spam messages being incomprehensible or adding a lot of extra artifacts such URL links. """)
            
            Num_Spam = len(Spam_Messages)
            Ave_Spam_Word_Count = Spam_Messages['num_words'].sum() / Num_Spam

            Num_Ham_Spam = len(Ham_Messages)
            Ave_Ham_Word_Count = Ham_Messages['num_words'].sum() / Num_Ham_Spam
            
            Y = [Ave_Ham_Word_Count, Ave_Spam_Word_Count]
   
            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average word count, Spam vs Ham")
            st.pyplot(fig)
            


        elif choice == "Figure 4 : Special Character Count":
            st.write(""" Spam messages often contain more special characters beause they are trying to bypass filters 
                     in email systems or increase likelihood of engagement.""")

            Ave_Spam_Mes_Spec_Chars = Spam_Messages['num_spec_chars'].sum() / Num_Spam

            Ave_Ham_Mes_Spec_Chars = Ham_Messages['num_spec_chars'].sum() / Num_Ham_Spam
            
            Y = [Ave_Ham_Mes_Spec_Chars,Ave_Spam_Mes_Spec_Chars]
        
            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average Special character count, Spam vs Ham")
            st.pyplot(fig)
            

        elif choice == "Figure 5 : Number of Digits":
            st.write("""Ham Messagse have far less digits or numbers in them cpmpared to spam. 
                     Threat actors commonly use an excessive amount of digits to evade spam filters. In some cases, Scammers
                     might be trying to spoof a legitimate number.""")

            Ave_Spam_Mes_Digits = Spam_Messages['num_digits'].sum() / Num_Spam

            Ave_Ham_Mes_Digits = Ham_Messages['num_digits'].sum() / Num_Ham_Spam
           
            Y = [Ave_Ham_Mes_Digits,Ave_Spam_Mes_Digits]
        
            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average digit count, Spam vs Ham")
            st.pyplot(fig)
           


        elif choice == "Figure 6 : Uppercase Word Count":
            st.write(""" The use of uppercase words can create a sense of urgency or pressure and often get users to engage with a message more.""")
        
            Ave_Spam_Upper_Words = Spam_Messages['num_Uppercase_Words'].sum() / Num_Spam

            Ave_Ham_Upper_Words = Ham_Messages['num_Uppercase_Words'].sum() / Num_Ham_Spam
            
            Y = [Ave_Ham_Upper_Words,Ave_Spam_Upper_Words]

            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average Uppercase Word count, Spam vs Ham")
            st.pyplot(fig)
            


        elif choice == "Figure 7 : URL Count":
            st.write(""" Malicious urls are rampant in emails as this is one of most common mediums for hackers to deliver harmful software such as trojans or viruses.  """)

            Ave_Spam_URLS = Spam_Messages['num_URLS'].sum() / Num_Spam

           
            Ave_Ham_URLS = Ham_Messages['num_URLS'].sum() / Num_Ham_Spam
            
            Y = [Ave_Ham_URLS,Ave_Spam_URLS]
        
            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average URL count, Spam vs Ham")
            st.pyplot(fig)
           
    
        elif choice == "Figure 8 : Email address Count":
            st.write("""Multiple email addresses being used in a message can maximize the audience reached by spam email.
                     This can also help obscure the sender's true identity.""")

            Ave_Spam_Emails = Spam_Messages['num_Emails'].sum() / Num_Spam

            Ave_Ham_Emails = Ham_Messages['num_Emails'].sum() / Num_Ham_Spam
            
            Y = [Ave_Ham_Emails,Ave_Spam_Emails]

            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average Email count, Spam vs Ham")
            st.pyplot(fig)
            

        elif choice == "Figure 9 : Suspcious Word Count":
            st.write(""" The use of profanity or other words like 'free' or 'YOU WON' can increase the likelihoof of engagement. Again, in some cases, 
                     this type of wording might help bypass filters. """)
            
            Ave_Sus_Words_Spam = Spam_Messages['num_Sus_Words'].sum() / Num_Spam

            Ave_Sus_Words_Ham = Ham_Messages['num_Sus_Words'].sum() / Num_Ham_Spam
            
            Y = [Ave_Sus_Words_Ham,Ave_Sus_Words_Spam]
        # Create figure explicitly
            fig, ax = plt.subplots(figsize=(3,3))
            sns.barplot(x=categories, y= Y, ax=ax)
            
            ax.set_xlabel('Message type')
            ax.set_ylabel('Amount')
            ax.set_title("Average Suspcious word count, Spam vs Ham")
            st.pyplot(fig)
            


