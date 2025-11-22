import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Cost Predictor Latur SubBranch", layout="wide")

st.title("💰 Health Insurance Cost Predictor")
st.markdown("Predict your health insurance cost based on your profile and lifestyle.")

# -----------------------
# Personal Information
# -----------------------
with st.expander("👤 Personal Information", expanded=True):
    age = st.slider("Age", min_value=18, max_value=100, value=25)
    gender = st.radio("Gender", ['Male', 'Female'])
    marital_status = st.radio("Marital Status", ['Unmarried', 'Married'])
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=20, step=1)

# -----------------------
# Health Information
# -----------------------
with st.expander("🩺 Health Information", expanded=True):
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
    smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])
    genetical_risk = st.slider("Genetical Risk (0-5)", 0, 5, 0)
    medical_history = st.selectbox(
        "Medical History",
        [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease',
            'Diabetes & Thyroid', 'Diabetes & Heart disease'
        ]
    )

# -----------------------
# Lifestyle & Finance
# -----------------------
with st.expander("💼 Lifestyle & Finance", expanded=True):
    income_lakhs = st.slider("Income (in Lakhs)", 0, 200, 10)
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])
    region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])

# -----------------------
# Prediction Button
# -----------------------
st.markdown("---")
if st.button("Predict Insurance Cost 💸"):
    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }
    prediction = predict(input_dict)
    st.success(f"🏥 Predicted Health Insurance Cost: {prediction}")
