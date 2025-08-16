# 📩 Spam vs Ham Classifier

## 📌 Project Overview
This project explores the classic **Spam vs Ham SMS classification problem** using **Natural Language Processing (NLP)** and **Machine Learning**.  
I not only trained models on the standard dataset but also stress-tested them with **generative AI–augmented datasets** (stricter imbalance + adversarial samples).  

The following is worflow for this project: **EDA → Preprocessing → Modeling → Testing** pipeline, with additional focus on **A/B testing for class imbalance** and **generalization beyond the training corpus**.  

---

## 📂 Dataset
- **Primary Dataset**: [SMS Spam Collection Dataset (UCI)](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)  
  - 5,574 labeled SMS messages  
  - Labels: `ham` (legit) vs `spam` (unwanted/malicious)  
  - Imbalance: ~87% ham vs ~13% spam  

- **Synthetic Datasets (Generated with LLMs)**:  
  1. **Similar Dataset** – SMS-like, different from training set, with stricter class imbalance.  
  2. **Adversarial Dataset** – Contains hacker/threat-actor artifacts (e.g., obfuscation, Neutral Language Injection).  

---

## 🛠 Workflow

### 1. EDA
- Explored spam vs ham messages **before preprocessing**.  
- Engineered new features, such as:  
  - Message length  
  - Presence of URLs
  - Digit and special-character ratios  
  - Presence of spam keywords  

---

### 2. Text Preprocessing
- Removed redundant signals from raw text (to avoid feature leakage).  
- Vectorized text using **CountVectorizer**.  
- Combined CountVectorizer output with **engineered features** → created final feature matrix for modeling.  

---

### 3. Modeling (with A/B Testing)
- **Models compared**: Naïve Bayes, Logistic Regression  
- **Experiment A**: Trained and evaluated models on **non-SMOTE** dataset  
- **Experiment B**: Trained and evaluated models on **SMOTE-augmented** dataset  
- **Findings**:  
  - Both models performed **very well without SMOTE**.  
  - SMOTE did not significantly improve performance — strong feature engineering likely compensated for class imbalance.  

---

### 4. Testing on New Datasets
- When tested on **synthetic similar** and **adversarial datasets**, models performed **poorly**.  
- Insight: While models fit the training data well, they **did not generalize** — highlighting the need for **stronger, more universal features**.  

---

## 📊 Key Results
- Naïve Bayes and Logistic Regression achieved **high Precision, Recall and F1-scores on original dataset** (with and without SMOTE).  
- Performance **dropped sharply on synthetic and adversarial datasets**.  
- This reveals that **robust generalization** can be more important than resampling methods like SMOTE in real-world applications.  

---

## 🔮 Future Work
To improve feature construction and generalization, I plan to explore:  
1. **TF-IDF** – better word weighting vs CountVectorizer.  
2. **N-gram & Collocation Analysis** – capture context and statistically significant multi-word patterns.  
3. **Type-Token Ratio** – detect repetitiveness, often present in spam.  
4. **Readability Metrics** – since spam often contains hard-to-read or incomprehensible text.  

---

## 🚀 Tech Stack
- **Languages & Libraries**: Python, Pandas, Matplotlib, Seaborn, Regex, Scikit-learn, Imbalanced-learn, Streamlit  
- **Models**: Naïve Bayes, Logistic Regression  
- **Deployment**: Streamlit for interactive app  

---
### Dataset Citation
- Almeida, T. & Hidalgo, J. (2011). SMS Spam Collection [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84.
----
## 📷 Demo
👉 [Insert Screenshot or GIF of Streamlit App Here]  

---

## 📁 Repository Structure
