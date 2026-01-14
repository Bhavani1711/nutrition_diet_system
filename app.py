import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Clinical Nutrition System", layout="centered")
st.title("Hospital Nutrition Recommendation System ")

patient_name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
concern = st.text_area("Enter Medical Condition / Concern")

def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()["response"]

if st.button("Generate AI Diet Plan"):
    if patient_name and concern:
        with st.spinner("AI Doctor is preparing personalized diet..."):
            prompt = f"""
You are a clinical nutrition expert AI in a hospital.

Patient Name: {patient_name}
Age: {age}
Gender: {gender}
Medical Concern: {concern}

Generate:
1. Foods to Eat (bullet points)
2. Foods to Avoid (bullet points)
3. Sample One Day Diet Plan (Breakfast, Lunch, Dinner)
4. Why this diet helps (medical reasoning)

Keep it safe, professional, and concise.
"""

            ai_response = query_ollama(prompt)

            st.subheader("Clinical Diet Plan")
            st.write(ai_response)
    else:
        st.warning("Please fill all patient details.")

