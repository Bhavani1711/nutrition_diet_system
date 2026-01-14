# import streamlit as st

# st.set_page_config(page_title="AI Nutrition System", layout="centered")

# st.title("🏥 AI Powered Nutrition & Diet Recommendation System")

# name = st.text_input("Enter Patient Name")
# concern = st.selectbox(
#     "Select Health Concern",
#     ["Diabetes", "PCOS", "Anemia", "Obesity", "Hypertension", "Acne", "General Fitness"]
# )

# def get_diet(concern):
#     data = {
#         "Diabetes": {
#             "eat": ["Oats", "Brown rice", "Leafy vegetables", "Bitter gourd", "Nuts"],
#             "avoid": ["Sugar", "White bread", "Soft drinks", "Fried food"],
#             "plan": "Breakfast: Oats | Lunch: Brown rice + Veg | Dinner: Soup + Salad"
#         },
#         "PCOS": {
#             "eat": ["Fruits", "Vegetables", "Whole grains", "Seeds"],
#             "avoid": ["Junk food", "Sugary items", "Refined carbs"],
#             "plan": "Breakfast: Fruits + Nuts | Lunch: Roti + Sabzi | Dinner: Light soup"
#         },
#         "Anemia": {
#             "eat": ["Spinach", "Beetroot", "Dates", "Pomegranate", "Lentils"],
#             "avoid": ["Tea with meals", "Processed food"],
#             "plan": "Breakfast: Dates + Milk | Lunch: Dal + Greens | Dinner: Roti + Veg"
#         },
#         "Obesity": {
#             "eat": ["Salads", "Fruits", "Boiled vegetables", "Protein"],
#             "avoid": ["Fast food", "Sugar", "Fried food"],
#             "plan": "Breakfast: Fruits | Lunch: Salad + Protein | Dinner: Soup"
#         },
#         "Hypertension": {
#             "eat": ["Banana", "Garlic", "Oats", "Low salt foods"],
#             "avoid": ["Salt", "Pickles", "Processed food"],
#             "plan": "Breakfast: Oats | Lunch: Rice + Veg | Dinner: Light meal"
#         },
#         "Acne": {
#             "eat": ["Water", "Fruits", "Vegetables", "Omega-3 foods"],
#             "avoid": ["Dairy", "Junk food", "Oily food"],
#             "plan": "Breakfast: Fruits | Lunch: Veg meal | Dinner: Light soup"
#         },
#         "General Fitness": {
#             "eat": ["Balanced diet", "Protein", "Fruits", "Vegetables"],
#             "avoid": ["Excess sugar", "Alcohol"],
#             "plan": "Breakfast: Eggs + Toast | Lunch: Rice + Chicken | Dinner: Salad"
#         }
#     }
#     return data[concern]

# if st.button("Generate Diet Plan"):
#     if name:
#         result = get_diet(concern)

#         st.subheader(f"Patient: {name}")
#         st.markdown(f"### 🥗 Foods to Eat")
#         for food in result["eat"]:
#             st.write("✔️", food)

#         st.markdown(f"### 🚫 Foods to Avoid")
#         for food in result["avoid"]:
#             st.write("❌", food)

#         st.markdown(f"### 📅 Sample Daily Plan")
#         st.success(result["plan"])
#     else:
#         st.warning("Please enter patient name.")

import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Clinical Nutrition System", layout="centered")
st.title("🏥 AI Powered Hospital Nutrition Recommendation System (Free LLM)")

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

            st.subheader("🧠 AI Generated Clinical Diet Plan")
            st.write(ai_response)
    else:
        st.warning("Please fill all patient details.")

