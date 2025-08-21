import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer # this will apply count vectorization to the text
from joblib import load

# this function will convert the text data to a dataframe 
def text_to_dataframe(File_Name):
    messages_and_results=[]

    # The following code create a list of dictionaries in the following form {message, whther message is spam or not}
    with open(File_Name,'r') as Spam_File:
        lines=Spam_File.readlines()
        for text in lines:
            if text.startswith("ham"):
                result="ham"
                text=text.replace(result,'',1) # remove the key from the text
                message=text.strip() # non-spam text accompanying the key, removes newlines,tabs, and spaces
                messages_and_results.append({'Text':message,'Result': result})
            elif text.startswith("spam"):
                result="spam"
                text=text.replace(result,'',1) # remove the key from the text
                message=text.strip() # non-spam text accompanying the key
                messages_and_results.append({'Text':message,'Result': result})
        
    df=pd.DataFrame(messages_and_results)
            
    return df

# ------------ helper functions to derive features in the text data-------------------

def Word_Count(message):
    return len(re.findall(r"\b[a-zA-Z']+\b" , message)) # counts the number of words in the message

def spec_char_check(message):
    return len(re.findall(r'[^a-zA-Z0-9\s]', message)) # counts the number of special characters in the text like '@' or '!'

def digit_check(message):
    return len(re.findall(r'\d', message)) # counts the number of digits in the message

def Upper_Count(message):
    return len(re.findall(r'\b[A-Z]+\b', message)) # counts the number of uppercase words in the message

def URL_Count(message):
    return len(re.findall(r'(https?://\S+|www\.\S+)', message)) # counts the number of urls in the message

def Email_Count(message):
    return len(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', message, flags=re.IGNORECASE)) # counts email addresses in message


def Monetary_Scams(message):
    # Words related to monetery scams
    message = message.lower()
    Suspicious_Monetary_Words = [
    "free", "win", "winner", "winnings", "cash", "bonus",
    "prize", "reward", "offer", "exclusive", "guarantee",
    "100% free", "earn", "earn money", "income", "double your",
    "get paid", "giveaway", "cheap", "lowest price"
    ]

    word_count = 0

    for word in Suspicious_Monetary_Words:
        if word in message:
            word_count+=1

    return word_count

def Urgency_Words(message):
    # words to induce urgency and pressure

    message = message.lower()
    Suspicious_Urgency_Words = [
    "urgent", "act now", "immediately", "don't miss", "limited time",
    "important", "as seen on", "last chance", "once in a lifetime",
    "apply now", "instant access", "final notice", "only today"
    ]

    word_count = 0

    for word in Suspicious_Urgency_Words:
        if word in message:
            word_count+=1

    return word_count

def Security_Scams(message):
    # words related to Security, scams and risky language

    message = message.lower()
    Suspicious_Security_Words = [
    "confidential", "risk-free", "no obligation", "guaranteed",
    "safe", "access now", "click below", "click here", "this isn’t spam",
    "unsubscribe", "why pay more", "credit card", "urgent response needed",
    "act immediately", "no cost"
    ]


    word_count = 0

    for word in Suspicious_Security_Words:
        if word in message:
            word_count+=1

    return word_count



def Health_Scams(message):
    # words related to health scams, drug use,etc

    message = message.lower()
    Suspicious_Health_Words = [
    "viagra", "cialis", "pills", "pharmacy", "meds", "enhancement",
    "lose weight", "no prescription", "miracle", "adult", "xxx",
    "nude", "satisfaction guaranteed"
    ]

    word_count = 0

    for word in Suspicious_Health_Words:
        if word in message:
            word_count+=1

    return word_count

def Digital_Scams(message):
    # words related to digital scams

    message = message.lower()
    Suspicious_Digital_Words = [
    "viagra", "cialis", "pills", "pharmacy", "meds", "enhancement",
    "lose weight", "no prescription", "miracle", "adult", "xxx",
    "nude", "satisfaction guaranteed"
    ]

    word_count = 0

    for word in Suspicious_Digital_Words:
        if word in message:
            word_count+=1

    return word_count



def Profanities_Count(message):
    # words related to explicit language

    message = message.lower()
    curse_words = [
    "bitch", "asshole", "shit", "fuck", "bastard", "dick", "crap", 
    "slut", "whore", "damn", "piss", "motherfucker", "cunt", "fag"
    ]
    
    word_count = 0

    for word in curse_words:
        if word in message:
            word_count+=1

    return word_count



def Suspicious_Word_Count(message): # combines all suspicious word functions into one function
    Sus_Word_Count = 0
    Sus_Word_Count = Monetary_Scams(message) + Urgency_Words(message) + Security_Scams(message) + Health_Scams(message) + Digital_Scams(message) + Profanities_Count(message)
    return Sus_Word_Count



def Transform_Target_Spam(text): # binary encoder for target variable
    if text.lower() == 'spam':
        return 1
    if text.lower() == 'ham':
        return 0


def Sus_Removal(text):
    Sus_Words = [
    "free", "win", "winner", "winnings", "cash", "bonus",
    "prize", "reward", "offer", "exclusive", "guarantee",
    "100% free", "earn", "earn money", "income", "double your",
    "get paid", "giveaway", "cheap", "lowest price","urgent", "act now", "immediately", "don't miss", "limited time",
    "important", "as seen on", "last chance", "once in a lifetime",
    "apply now", "instant access", "final notice", "only today","confidential", "risk-free", "no obligation", "guaranteed",
    "safe", "access now", "click below", "click here", "this isn’t spam",
    "unsubscribe", "why pay more", "credit card", "urgent response needed",
    "act immediately", "no cost","viagra", "cialis", "pills", "pharmacy", "meds", "enhancement",
    "lose weight", "no prescription", "miracle", "adult", "xxx",
    "nude", "satisfaction guaranteed","viagra", "cialis", "pills", "pharmacy", "meds", "enhancement",
    "lose weight", "no prescription", "miracle", "adult", "xxx",
    "nude", "satisfaction guaranteed","bitch", "asshole", "shit", "fuck", "bastard", "dick", "crap", 
    "slut", "whore", "damn", "piss", "motherfucker", "cunt", "fag"
    ]
    for word in Sus_Words:
        text = re.sub(r'\b' + re.escape(word) + r'\b', '', text)

    return text

def clean_text(text): # remove redundant signals from text data 
    text = text.lower() # remove uppercasewords
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = re.sub(r'\S+@\S+', '', text)  # Remove emails
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r"[^a-z\s]", '', text)  # Remove punctuation/numbers
    text = Sus_Removal(text) # remove any suspicious words from the text
    return text.strip()


#---------------------------------------------------------------------------------------

# function that applies helper functions to a given dataframe for feature engineering
def Spam_Feature_Engineering(DataFrame):
    DataFrame['num_chars'] = DataFrame['Text'].apply(len) # gathers number of characters in the text and makes a new feature called 'num_chars'
    DataFrame['num_words'] = DataFrame['Text'].apply(Word_Count) # counts the words in the message and makes a new feature called 'num_words'
    DataFrame['num_spec_chars'] = DataFrame['Text'].apply(spec_char_check) # counts the special characters in the message and makes a new feature called 'num_spec_chars'
    DataFrame['num_digits'] = DataFrame['Text'].apply(digit_check) # counts the digits in the message and makes a new feature called 'num_digits'
    DataFrame['num_Uppercase_Words'] = DataFrame['Text'].apply(Upper_Count) # uppercase word count in the message and makes a new feature called 'num_Uppercase_Words'
    DataFrame['num_URLS'] = DataFrame['Text'].apply(URL_Count) # counts number of urls then creates new feature called 'num_URLS'
    DataFrame['num_Emails'] = DataFrame['Text'].apply(Email_Count) # counts number of emaill addresses then creates new feature called 'num_Emails'
    DataFrame['num_Sus_Words'] = DataFrame['Text'].apply(Suspicious_Word_Count) # suspicious word count , makes new feature called 'num_Sus_Words'
    DataFrame['Result'] = DataFrame['Result'].apply(Transform_Target_Spam) # binary encodes the target variable
    
    return DataFrame


def SpamData_Preprocessor(FileName):
    Vector = load('Streamlit_App/Models/Vectorizer.joblib')
    
    Spam_df = text_to_dataframe(FileName) # convert text file to dataframe
    Spam_df = Spam_Feature_Engineering(Spam_df) # apply feature engineering
    Spam_df['Text'] = Spam_df['Text'].apply(clean_text) # remove redundant signals from the message

    # lets vectorize the text and convert to a dataframe
    #Vectorizer = CountVectorizer(stop_words='english',max_features=5000) # create vectorizer
    X_text = Vector.transform(Spam_df['Text']) # create sparse matrix
    X_text_df = pd.DataFrame(X_text.toarray(), columns=Vector.get_feature_names_out()) # convert sparse matrix to dataframe
    Spam_df = pd.concat([Spam_df.reset_index(drop=True), X_text_df.reset_index(drop=True)], axis=1) # combine vectorized dataframe with original dataframe
    Spam_df = Spam_df.drop(['Text'],axis =1) # remove the 'Text' column
    return Spam_df





#-------------- functions for Streamlit spam prediction ___________________________________

def Message_Feature_Engineering(DataFrame):
    DataFrame['num_chars'] = DataFrame['Text'].apply(len) # gathers number of characters in the text and makes a new feature called 'num_chars'
    DataFrame['num_words'] = DataFrame['Text'].apply(Word_Count) # counts the words in the message and makes a new feature called 'num_words'
    DataFrame['num_spec_chars'] = DataFrame['Text'].apply(spec_char_check) # counts the special characters in the message and makes a new feature called 'num_spec_chars'
    DataFrame['num_digits'] = DataFrame['Text'].apply(digit_check) # counts the digits in the message and makes a new feature called 'num_digits'
    DataFrame['num_Uppercase_Words'] = DataFrame['Text'].apply(Upper_Count) # uppercase word count in the message and makes a new feature called 'num_Uppercase_Words'
    DataFrame['num_URLS'] = DataFrame['Text'].apply(URL_Count) # counts number of urls then creates new feature called 'num_URLS'
    DataFrame['num_Emails'] = DataFrame['Text'].apply(Email_Count) # counts number of emaill addresses then creates new feature called 'num_Emails'
    DataFrame['num_Sus_Words'] = DataFrame['Text'].apply(Suspicious_Word_Count) # suspicious word count , makes new feature called 'num_Sus_Words'
    
    
    return DataFrame

def Message_to_dataframe(text):

    messages_and_results=[]

    message=text.strip() # non-spam text accompanying the key, removes newlines,tabs, and spaces
    messages_and_results.append({'Text':message})
            
        
    df=pd.DataFrame(messages_and_results)
            
    return df

def Message_Preprocessor(message):
    # This helps to preprocess messages fed into the streamlit app before before processed by our model
    Vector = load('Streamlit_App/Models/Vectorizer.joblib')
    
    Spam_df = Message_to_dataframe(message) # convert text file to dataframe
    Spam_df = Message_Feature_Engineering(Spam_df) # apply feature engineering
    Spam_df['Text'] = Spam_df['Text'].apply(clean_text) # remove redundant signals from the message

    # lets vectorize the text and convert to a dataframe
    #Vectorizer = CountVectorizer(stop_words='english',max_features=5000) # create vectorizer
    X_text = Vector.transform(Spam_df['Text']) # create sparse matrix
    X_text_df = pd.DataFrame(X_text.toarray(), columns=Vector.get_feature_names_out()) # convert sparse matrix to dataframe
    Spam_df = pd.concat([Spam_df.reset_index(drop=True), X_text_df.reset_index(drop=True)], axis=1) # combine vectorized dataframe with original dataframe
    Spam_df = Spam_df.drop(['Text'],axis =1) # remove the 'Text' column
    return Spam_df
    
    
    
#---------------------------------------------------

# This function is specifically for model comaprisons in F5_Model_Comparisons.py, 
# 03_Spam_Preprocess_Phase.csv is too a big a file to upload on github

def Model_Comp_Preprocessor(Spam_df):
    # This helps to preprocess messages fed into the streamlit app before before processed by our model
    Vector = load('Streamlit_App/Models/Vectorizer.joblib')
    Spam_df['Result'] = Spam_df['Result'].apply(Transform_Target_Spam)
    Spam_df['Text'] = Spam_df['Text'].apply(clean_text) # remove redundant signals from the message

    # lets vectorize the text and convert to a dataframe
    #Vectorizer = CountVectorizer(stop_words='english',max_features=5000) # create vectorizer
    X_text = Vector.transform(Spam_df['Text']) # create sparse matrix
    X_text_df = pd.DataFrame(X_text.toarray(), columns=Vector.get_feature_names_out()) # convert sparse matrix to dataframe
    Spam_df = pd.concat([Spam_df.reset_index(drop=True), X_text_df.reset_index(drop=True)], axis=1) # combine vectorized dataframe with original dataframe
    Spam_df = Spam_df.drop(columns=['Text'], errors='ignore') # remove the 'Text' column
    return Spam_df
    




