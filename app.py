import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Load your model and scaler
model = load_model('credit_risk_model.h5')
scaler = joblib.load('scaler.pkl')


# Set up the app layout
st.title("💳 Credit Risk Profiler 💳")
st.sidebar.header("📊 Input Features")

# Collect user input for each feature
revolving_utilization = st.sidebar.slider(
    'Current Credit Usage (% of limit)', 0.0, 1.0, 0.5,
    help="Proportion of credit limit currently in use"
)
age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)

debt_ratio = st.sidebar.slider('Debt Ratio', 0.0, 1.0, 0.3)

open_credit_lines = st.sidebar.number_input(
    ' Number of Active Credit Cards / Loans',
    min_value=1, max_value=20, value=5,
    help="This includes active credit cards, car loans, student loans, etc."
)
real_estate_loans = st.sidebar.number_input(
    'Number of Home Loans or Mortgages',
    min_value=0, max_value=5, value=1,
    help="Includes mortgages, home equity lines of credit, or any loans related to real estate."
)

time_30_59_days_past_due = st.sidebar.number_input('Number of Late Payments', min_value=0, max_value=30, value=0)
monthly_income = st.sidebar.number_input('Monthly Income Per Person ($)', min_value=0, value=50000)
# Create a list of features
features = np.array([
    float(revolving_utilization), float(age), float(debt_ratio), float(open_credit_lines), float(real_estate_loans),float(time_30_59_days_past_due),float(monthly_income)
])


# Scale the input data
scaled_features = scaler.transform([features])

# Predict the risk level using the model
prediction = model.predict(scaled_features)
risk_label = np.argmax(prediction, axis=1)[0]

# Map the risk level to its respective label
risk_labels = {0: 'Low', 1: 'Medium', 2: 'High'}
risk = risk_labels[risk_label]

# Display prediction
st.subheader(f"📝 Predicted Risk Level")
if risk== "Low":
        st.success("""The risk level of this applicant is predicted to be Low
        """)

elif risk == "Medium":
        st.warning("""
        The risk level of this applicant is predicted to be Medium
        """)

elif risk == "High":
        st.error("""
        The risk level of this applicant is predicted to be High
        """)


# Add some additional info
st.markdown("### 📉 Model Explanation")
st.write("This model uses several financial features such as debt ratio, age, income, and payment history to predict the applicant's credit risk.")
st.markdown("### 📌 Disclaimer")
st.write("This is a demonstration of a machine learning model predicting credit risk. It should not be used for actual financial decisions.")
