# Credit Risk Profiler — Machine Learning Web App for Loan Default Prediction 

A **Streamlit-powered machine learning application** that predicts whether a loan applicant is likely to default, using **XGBoost classification** on financial and credit-related data.  

Built to assist **banks and financial institutions** in making faster, data-driven lending decisions.

---

##  Live Demo
[![Streamlit App](https://img.shields.io/badge/Try%20the%20App-Streamlit-blue?logo=streamlit)](https://credit-risk-profiler-ecaxbstztixgzhyxbe9xhv.streamlit.app/)

---

##  Key Features
- **Fast Loan Risk Prediction** using an optimized XGBoost Classifier  
- **Balanced Dataset Handling** with undersampling to reduce bias in predictions  
- **Professional Banking-Themed UI** for a clean and intuitive user experience  
- **High Precision & Recall** for both “Default” and “Not Default” classes  
- **Deployed on Streamlit Community Cloud** — accessible from any browser  

---

## Problem & Solution
Loan default prediction is critical for minimizing financial risk while ensuring fair access to credit.  

This tool helps lending teams **quickly assess borrower risk** using historical patterns, improving decision-making and reducing manual evaluation time.

---

##  ML Workflow
1. **Data Preprocessing**  
   - Removed non-informative columns based on correlation and domain knowledge  
   - Handled missing values using median imputation  
   - Balanced classes via random undersampling to improve recall for minority class  

2. **Model Development**  
   - Algorithm: XGBoost Classifier for binary classification  
   - Metrics: Precision, Recall, and F1-score to evaluate model robustness  

3. **Deployment**  
   - UI: Streamlit with a clean, banking-inspired theme  
   - Hosting: Streamlit Community Cloud with serialized model using Joblib  

---

## Input Parameters

| Feature               | Description                                  |
|-----------------------|----------------------------------------------|
| Home Ownership        | Rent / Mortgage / Own / Other                |
| Employment Length     | Duration of employment in months             |
| Loan Grade            | Creditworthiness category of the borrower    |
| Loan Amount           | Total loan amount requested                  |
| Interest Rate         | Loan interest rate                           |
| Loan Approval Status  | 0 = Not approved, 1 = Approved                |
| Loan % of Income      | Loan amount as a percentage of borrower income|

---

## Output

| Output Metric        | Description                                    |
|----------------------|------------------------------------------------|
| Default Prediction   | 0 = Default Likely, 1 = Not Default Likely     |
| Risk Explanation     | Interpretable output indicating decision basis |

---

## Tech Stack

**Languages & Libraries**  
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)  
Pandas • NumPy • Scikit-learn • XGBoost  

**Deployment**  
Streamlit • Joblib  

---

## 👩‍💻 Author
**Shreiya Muthuvelan**  
2nd Year CSE @ BITS Pilani Dubai 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/shreiyamuthuvelan)  

---
