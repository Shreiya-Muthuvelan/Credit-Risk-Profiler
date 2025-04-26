# 💳 Credit Risk Profiler 🏦

An intelligent **XGBoost-based classification system** that predicts whether an individual is likely to default on a loan, using financial and credit-related data. Designed to support banks and financial institutions in making fast, data-driven lending decisions.

---

## 🚀 Demo

🔗 Try the app here:([credit-risk-profiler-garxdeglbsx2qzkdatghu6](https://credit-risk-profiler-ecaxbstztixgzhyxbe9xhv.streamlit.app/))

---

## 📌 Features

- **XGBoost Classifier** trained to detect loan default risk (Binary classification)  
- Handles class imbalance using undersampling
- **Predicts loan default status**: Default (0) or Not Default (1)  
- Clean, intuitive Streamlit Web App with a professional banking-themed UI
- Model Evaluation with strong precision & recall across both classes

---
## 🧠 ML Workflow

1. **Data Preprocessing**
   - Removed irrelevant columns and handled missing values
   - Addressed class imbalance via undersampling

2. **Modeling**
   - Built an XGBClassifier using XGBoost
   - Evaluated using precision, recall, and F1-score

3. **Deployment**
   - Developed an interactive Streamlit UI with a clean banking theme
   - Deployed on **Streamlit Community Cloud** for public access

---

## 📥 Input Parameters

| Feature               | Description                            |
|-----------------------|----------------------------------------|
| Home Ownership        | (Rent / Mortgage / Own / Other)        |
| Employment Length     | Length of Employement (in months)      |
| Loan Grade            | Credit Worthiness of Borrower          |
| Loan Amount           | Amount of Loan                         |
| Interest Rate         | Interest rate of the loan              |
| Loan Approval Status  | Not approved(0) / Approved(1)          |
| Loan Percent of Income| Loan amount as a percentage of income  |

---
## 📤 Output

- `Binary Prediction` if the applicant is likely to default or not

---

## 🗂️ Technologies Used

- Python 
- TensorFlow / Keras  
- Pandas & NumPy  
- Scikit-learn
- XGBoost
- Streamlit  
- Joblib 

---

## 👩‍💻 Author

**Shreiya**  
2nd Year CSE Student | ML Enthusiast  
📍 BITS Pilani Dubai Campus  
🔗 [LinkedIn](https://www.linkedin.com/in/shreiyamuthuvelan)

---


