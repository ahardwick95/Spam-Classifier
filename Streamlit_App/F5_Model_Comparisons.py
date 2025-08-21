import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score
from Scripts.Spam_Preprocessor import Model_Comp_Preprocessor
from joblib import load

def Model_Comparisons():
    st.markdown("<h1 style='text-align: center;'>Model Comparisons</h1>", unsafe_allow_html=True)

    #load the models
    Bayes = load('Streamlit_App/Models/Bayes_Model.joblib')
    LogReg = load('Streamlit_App/Models/LogReg_Model.joblib')

    #load the dataset
    Spam_df = pd.read_csv('Streamlit_App/Data/02_Spam_EDA_Phase.csv')
    Spam_df = Model_Comp_Preprocessor(Spam_df)

    # separate into freatures and target variable
    Y = Spam_df['Result']
    X = Spam_df.drop(['Result'], axis=1)

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


    # THe following is done in each column
    # Target variable is calculated by logistic regression and naive bayes models
    # Then the metrics (i.e. Precision, Recall, F1-Score) is calculated
    # Ater this, the results are shown on doouble bar charts for comparisons for both Pre-SMOTE and SMOTE


    # ---------- Left Column: Pre-SMOTE ----------
    with col1:
        Y_Pred_Final = Bayes.predict(X)
        Y_Pred_Log_Final = LogReg.predict(X)

        precision_Bayes_Final = precision_score(Y, Y_Pred_Final, average='binary', pos_label=1)  
        recall_Bayes_Final = recall_score(Y, Y_Pred_Final, average='binary', pos_label=1)       
        f1_Bayes_Final = f1_score(Y, Y_Pred_Final, average='binary', pos_label=1) 

        precision_log_Final = precision_score(Y, Y_Pred_Log_Final, average='binary', pos_label=1)
        recall_log_Final = recall_score(Y, Y_Pred_Log_Final, average='binary', pos_label=1)       
        f1_log_Final = f1_score(Y, Y_Pred_Log_Final, average='binary', pos_label=1)

        metrics = ['Precision', 'Recall', 'F1-Score']

        Naive_Bayes_Scores = [precision_Bayes_Final, recall_Bayes_Final, f1_Bayes_Final]
        LogReg_Scores = [precision_log_Final, recall_log_Final, f1_log_Final]

        x = np.arange(len(metrics))  
        width = 0.35  

        fig, ax = plt.subplots(figsize=(6, 4))
        bars_a = ax.bar(x - width/2, Naive_Bayes_Scores, width, label='Naive Bayes', color='#1f77b4')
        bars_b = ax.bar(x + width/2, LogReg_Scores, width, label='LogReg', color='#ff7f0e')

        ax.set_xticks(x)
        ax.set_xticklabels(metrics, fontsize=11)
        ax.set_ylabel('Score', fontsize=11)
        ax.set_title('Model Comparison (Pre-SMOTE)', fontsize=13, pad=10)
        ax.legend(fontsize=10)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        add_labels(ax, bars_a)
        add_labels(ax, bars_b)

        st.pyplot(fig)

    # ---------- Right Column: SMOTE ----------
    with col2:
        metrics = ['Precision', 'Recall', 'F1-Score']

        Naive_Bayes_Scores_SMOTE = [0.952054794520548, 0.9210174029451138, 0.9291019581363943]
        LogReg_Scores_SMOTE = [0.9006369426751593, 0.9464524765729585, 0.922976501305483]

        x = np.arange(len(metrics))  
        width = 0.35  

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        bars_a2 = ax2.bar(x - width/2, Naive_Bayes_Scores_SMOTE, width, label='Naive Bayes', color='#1f77b4')
        bars_b2 = ax2.bar(x + width/2, LogReg_Scores_SMOTE, width, label='LogReg', color='#ff7f0e')

        ax2.set_xticks(x)
        ax2.set_xticklabels(metrics, fontsize=11)
        ax2.set_ylabel('Score', fontsize=11)
        ax2.set_title('Model Comparison (SMOTE)', fontsize=13, pad=10)
        ax2.legend(fontsize=10)
        ax2.grid(axis='y', linestyle='--', alpha=0.7)

        add_labels(ax2, bars_a2)
        add_labels(ax2, bars_b2)

        st.pyplot(fig2)

    st.write(""" In this case, SMOTE did not make that much difference in performance and in fact made it worse.
              For this case, it seems feature engineering was enough to distinguish between spam and ham( benign) messages.""")


