import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler


model = load_model('credit_risk_model.h5')
scaler = joblib.load('scaler.pkl')



st.title("💳 Credit Risk Profiler 💳")
st.markdown("### Predict the risk level of a loan application based on the applicant's financial data")
st.sidebar.header("📊 Input Features")

revolving_utilization = st.sidebar.slider('Revolving Utilization of Unsecured Lines', 0.0, 1.0, 0.5)
age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)
time_30_59_days_past_due = st.sidebar.number_input('Number of Time 30-59 Days Past Due Not Worse', min_value=0, max_value=30, value=0)
debt_ratio = st.sidebar.slider('Debt Ratio', 0.0, 1.0, 0.3)
monthly_income = st.sidebar.number_input('Monthly Income ($)', min_value=0, value=5000)
open_credit_lines = st.sidebar.number_input('Number of Open Credit Lines and Loans', min_value=1, max_value=20, value=5)
times_90_days_late = st.sidebar.number_input('Number of Times 90 Days Late', min_value=0, max_value=30, value=0)
real_estate_loans = st.sidebar.number_input('Number of Real Estate Loans or Lines', min_value=0, max_value=5, value=1)
time_60_89_days_past_due = st.sidebar.number_input('Number of Time 60-89 Days Past Due Not Worse', min_value=0, max_value=30, value=0)
num_dependents = st.sidebar.number_input('Number of Dependents', min_value=0, max_value=10, value=1)


features = np.array([
    float(revolving_utilization), float(age), float(time_30_59_days_past_due),
    float(debt_ratio), float(monthly_income), float(open_credit_lines),
    float(times_90_days_late), float(real_estate_loans), float(time_60_89_days_past_due),
    float(num_dependents)
])



scaled_features = scaler.transform([features])
prediction = model.predict(scaled_features)
risk_label = np.argmax(prediction, axis=1)[0]
risk_labels = {0: 'Low', 1: 'Medium', 2: 'High'}
risk = risk_labels[risk_label]

st.subheader(f"📝 Predicted Risk Level: {risk}")
st.write(f"The risk level of this applicant is predicted to be **{risk}** based on the input features.")
st.markdown("### 📉 Model Explanation")
st.write("This model uses several financial features such as debt ratio, age, income, and payment history to predict the applicant's credit risk.")
st.markdown("### 📌 Disclaimer")
st.write("This is a demonstration of a machine learning model predicting credit risk. It should not be used for actual financial decisions.")
