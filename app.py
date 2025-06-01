import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('model_pipeline.pkl')

# Judul
st.title("Customer Churn Prediction")

# Input user
gender = st.selectbox('Gender', ['Male', 'Female'])
SeniorCitizen = st.selectbox('Senior Citizen', [0, 1])
Partner = st.selectbox('Partner', ['Yes', 'No'])
Dependents = st.selectbox('Dependents', ['Yes', 'No'])
tenure = st.slider('Tenure', 0, 72, 1)
MonthlyCharges = st.number_input('Monthly Charges')
TotalCharges = st.number_input('Total Charges')

# ... tambahkan semua input sesuai fitur dari dataset

if st.button('Predict Churn'):
    input_df = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [SeniorCitizen],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'tenure': [tenure],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges],
        # tambahkan kolom lainnya
    })
    
    prediction = model.predict(input_df)[0]
    st.write('Churn' if prediction else 'Not Churn')
