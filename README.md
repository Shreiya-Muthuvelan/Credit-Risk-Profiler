# 💳 Credit Risk Profiler 🏦

An intelligent neural network-based system that predicts the **credit risk level**(Low, Medium, High)  of individuals using historical financial and credit-related data.It is designed to assist banks and financial institutions in quickly profiling clients and making data-driven decisions.

---

## 🚀 Demo

🔗 Try the app here: [https://subtle-sign-detector-ka9g5apjnjvkmvufuy8jow.streamlit.app/](https://credit-risk-profiler-ecaxbstztixgzhyxbe9xhv.streamlit.app/)

---

## 📌 Features

- 🧮 **Neural Network Classification Model** using TensorFlow/Keras  
- ⚖️ Tackles **class imbalance** using SMOTE  
- 🧼 Handles **missing values, scaling**, and preprocessing  
- 🎯 Predicts 3 classes: **Low**, **Medium**, and **High** credit risk  
- 🖥️ **Streamlit Web App** with an intuitive banking-themed UI  
- 📊 Model Evaluation: Precision, Recall, F1-score  

---
## 🧠 ML Workflow

1. **Data Preprocessing**
   - Removed irrelevant columns and handled missing values
   - Scaled features using `StandardScaler`
   - Applied **SMOTE** to balance class distribution

2. **Modeling**
   - Built a Neural Network using Keras with Dense layers
   - Used **Softmax** activation, `SparseCategoricalCrossentropy` loss, and `Adam` optimizer
   - Implemented **EarlyStopping** to reduce overfitting

3. **Deployment**
   - Developed an interactive Streamlit UI with a clean banking theme
   - Deployed on **Streamlit Community Cloud** for public access

---

## 🗂️ Technologies Used

- Python 
- TensorFlow / Keras  
- Pandas & NumPy  
- Scikit-learn
- Imbalanced-learn (SMOTE) 
- Streamlit  
- Joblib 

---

## 👩‍💻 Author

**Shreiya**  
2nd Year CSE Student | ML Enthusiast  
📍 BITS Pilani Dubai Campus  
🔗 [LinkedIn](https://www.linkedin.com/in/shreiyamuthuvelan)

---

