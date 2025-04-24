import streamlit as st
import numpy as np
import pickle
import joblib
st.set_page_config(page_title="💳 Credit Risk Profiler", layout="centered")
# Load the trained model and label encoders
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    encoders = joblib.load("label_encoders.pkl")  # dict of LabelEncoder objects
    return model, encoders

model, encoders = load_model()


st.title("🏦 Credit Risk Profiler")
st.markdown("### Get insights on loan applicant risk using ML predictions")
st.markdown("---")
st.sidebar.header("🔧 Input Features")

# Sliders and selectors for input
#person_age = st.sidebar.slider("👤 Age", 18, 100, 30)


home_ownership_display={"Mortgage 🏠": "MORTGAGE","Other 🏚️":"OTHER","Own 🔑":"OWN","Rent 🪟":"RENT"}

home_ownership_option = st.sidebar.radio("🏡 Home Ownership", list(home_ownership_display.keys()))
home_ownership_raw = home_ownership_display[home_ownership_option]
person_home_ownership = encoders['person_home_ownership'].transform([home_ownership_raw])[0]

person_emp_length = st.sidebar.slider("🧑‍💼 Employment Length (months)", 0, 123, 24)

loan_grade = st.sidebar.slider("📊 Loan Grade", 0, 6, 3)

loan_amnt = st.sidebar.slider("💵 Loan Amount ($)", 1000, 35000, 10000, step=500)
loan_int_rate = st.sidebar.slider("📈 Interest Rate (%)", 5.0, 23.0, 12.5)


loan_status_option = st.sidebar.radio("📑 Loan Approval Status", ["Not Approved ❌", "Approved ✅"])

# Map the user-friendly label to numerical value
loan_status = 1 if loan_status_option == "Approved ✅" else 0


loan_percent_income = st.sidebar.slider("💸 Loan Percent of Income", 0.0, 0.7, 0.2, step=0.01)

if st.button("🔍 Predict Credit Risk"):
    # Combine inputs
    input_data = np.array([[
        person_home_ownership,
        person_emp_length,
        loan_grade,
        loan_amnt,
        loan_int_rate,
        loan_status,
        loan_percent_income,
    ]],dtype=np.float32)

    # Make prediction
    prediction = model.predict(input_data)

    # Show result
    if prediction == 1:
        st.success("✅ Low Credit Risk: Applicant is unlikely to default.")
    else:
        st.error("⚠️ High Credit Risk: Applicant may default. Further review recommended.")
