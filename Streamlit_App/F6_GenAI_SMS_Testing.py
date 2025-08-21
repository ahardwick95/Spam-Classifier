import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score
from Scripts.Spam_Preprocessor import SpamData_Preprocessor
from joblib import load

def Gen_AI_Model_Comparisons():

    st.markdown("<h1 style='text-align: center;'>Generative Dataset Testing</h1>", unsafe_allow_html=True)

    # load up models
    Bayes = load('Streamlit_App/Models/Bayes_Model.joblib')
    LogReg = load('Streamlit_App/Models/LogReg_Model.joblib')

    # load and preprocess the new datasets
    Spam_df = SpamData_Preprocessor('Streamlit_App/Data/New_SMS_Dataset.txt')
    Adv_SMS_df = SpamData_Preprocessor('Streamlit_App/Data/Adversarial_SMS_Dataset.txt')

    # calculate the features and target variables for each datasets
    Y = Spam_df['Result']
    X = Spam_df.drop(['Result'], axis=1)

    Y_Adv = Adv_SMS_df['Result']
    X_Adv = Adv_SMS_df.drop(['Result'], axis=1)

    # Function to add labels on top of bars
    def add_labels(ax, bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10)

    col1, col2 = st.columns(2)

    # The following is done in each column
    # Target variable is calculated by logistic regression and naive bayes models
    # Then the metrics (i.e. Precision, Recall, F1-Score) is calculated
    # Ater this, the results are shown on doouble bar charts for comparisons for both new SMS dataset and adversarial dataset

    # ------ left column : new SMS dataset similar to original dataset-----------
    with col1:
        Y_Pred = Bayes.predict(X)
        Y_Pred_Log = LogReg.predict(X)

        precision_bayes = precision_score(Y, Y_Pred, average='binary', pos_label=1)
        recall_bayes = recall_score(Y, Y_Pred, average='binary', pos_label=1)       
        f1_bayes = f1_score(Y, Y_Pred, average='binary', pos_label=1) 

        precision_Log = precision_score(Y, Y_Pred_Log, average='binary', pos_label=1)
        recall_Log = recall_score(Y, Y_Pred_Log, average='binary', pos_label=1)       
        f1_Log = f1_score(Y, Y_Pred_Log, average='binary', pos_label=1) 

        metrics = ['Precision', 'Recall', 'F1-Score']

        Naive_Bayes_Scores = [precision_bayes,recall_bayes,f1_bayes]
        LogReg_Scores = [precision_Log,recall_Log,f1_Log]

        # Positions and width for bars
        x = np.arange(len(metrics))  # [0, 1, 2]
        width = 0.35  # Width of each bar

        # Plotting
        fig, ax = plt.subplots(figsize=(8, 5))
        bars_a = ax.bar(x - width/2, Naive_Bayes_Scores, width, label='Naive Bayes', color='#1f77b4')
        bars_b = ax.bar(x + width/2, LogReg_Scores, width, label='LogReg', color='#ff7f0e')

        # Customize the plot
        ax.set_xticks(x)
        ax.set_xticklabels(metrics, fontsize=12)
        ax.set_ylabel('Score', fontsize=12)
        ax.set_title('Model Comparison for Spam: Precision, Recall, F1-Score', fontsize=14, pad=15)
        ax.legend(fontsize=12)
        ax.grid(axis='y', linestyle='--', alpha=0.7)


        add_labels(ax, bars_a)
        add_labels(ax, bars_b)

        plt.tight_layout()

        st.pyplot(fig)

   
   #----------- Right column: adversarial dataset-------------------
    with col2:

        Y_Pred_Adv = Bayes.predict(X_Adv)
        Y_Pred_Log_Adv = LogReg.predict(X_Adv)

        precision_bayes_Adv = precision_score(Y_Adv, Y_Pred_Adv, average='binary', pos_label=1)
        recall_bayes_Adv = recall_score(Y_Adv, Y_Pred_Adv, average='binary', pos_label=1)       
        f1_bayes_Adv = f1_score(Y_Adv, Y_Pred_Adv, average='binary', pos_label=1)

        precision_Log_Adv = precision_score(Y_Adv, Y_Pred_Log_Adv, average='binary', pos_label=1)
        recall_Log_Adv = recall_score(Y_Adv, Y_Pred_Log_Adv, average='binary', pos_label=1)       
        f1_Log_Adv = f1_score(Y_Adv, Y_Pred_Log_Adv, average='binary', pos_label=1)

        metrics = ['Precision', 'Recall', 'F1-Score']

        Naive_Bayes_Scores = [precision_bayes_Adv,recall_bayes_Adv,f1_bayes_Adv]
        LogReg_Scores = [precision_Log_Adv,recall_Log_Adv,f1_Log_Adv]

        # Positions and width for bars
        x = np.arange(len(metrics))  # [0, 1, 2]
        width = 0.35  # Width of each bar

        # Plotting
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        bars_a = ax2.bar(x - width/2, Naive_Bayes_Scores, width, label='Naive Bayes', color='#1f77b4')
        bars_b = ax2.bar(x + width/2, LogReg_Scores, width, label='LogReg', color='#ff7f0e')

        # Customize the plot
        ax2.set_xticks(x)
        ax2.set_xticklabels(metrics, fontsize=12)
        ax2.set_ylabel('Score', fontsize=12)
        ax2.set_title('Model Comparison for Spam: Precision, Recall, F1-Score (adversarial)', fontsize=14, pad=15)
        ax2.legend(fontsize=12)
        ax2.grid(axis='y', linestyle='--', alpha=0.7)

        add_labels(ax2, bars_a)
        add_labels(ax2, bars_b)

        plt.tight_layout()
        st.pyplot(fig2)
    
    st.write("""As we can see , on the new dataset that is similar to the original dataset, logistic regression did relatively well naive bayes did not.

             However, on the adversarial dataset, naive bayes did far better then logistic regression. Overall, it can be said that niether model did not generalize as well as expected to the new datasets. """)

