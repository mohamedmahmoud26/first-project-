import streamlit as st
import pandas as pd
from model_utils import load_model, predict
import time
import matplotlib.pyplot as plt
# Load trained model
model = load_model()

# App Title
st.title("🎓 Student Performance Prediction App")
st.write("Predict the **final grade (G3)** of a student based on various personal and academic features.")

# User Data Entry Section
st.header("Enter Student Details")

# --- Personal Info ---
col1, col2, col3 = st.columns(3)
with col1:
    school = st.selectbox("School", ["GP", "MS"])
    sex = st.selectbox("Sex", ["F", "M"])
    age = st.number_input("Age", 15, 22, 17)
    address = st.selectbox("Address", ["U", "R"])
    famsize = st.selectbox("Family Size", ["LE3", "GT3"])
with col2:
    pstatus = st.selectbox("Parent Status", ["T", "A"])
    medu = st.selectbox("Mother Education", [0, 1, 2, 3, 4])
    fedu = st.selectbox("Father Education", [0, 1, 2, 3, 4])
    mjob = st.selectbox("Mother Job", ['teacher', 'health', 'services', 'at_home', 'other'])
    fjob = st.selectbox("Father Job", ['teacher', 'health', 'services', 'at_home', 'other'])
with col3:
    reason = st.selectbox("Reason for School Choice", ['home', 'reputation', 'course', 'other'])
    guardian = st.selectbox("Guardian", ['mother', 'father', 'other'])
    traveltime = st.selectbox("Travel Time", [1, 2, 3, 4])
    studytime = st.selectbox("Weekly Study Time", [1, 2, 3, 4])
    failures = st.number_input("Past Class Failures", 0, 4, 0)

# --- Supports & Lifestyle ---
col4, col5, col6 = st.columns(3)
with col4:
    schoolsup = st.selectbox("Extra Educational Support", ["yes", "no"])
    famsup = st.selectbox("Family Educational Support", ["yes", "no"])
    paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
    activities = st.selectbox("Extra-Curricular Activities", ["yes", "no"])
with col5:
    nursery = st.selectbox("Attended Nursery School", ["yes", "no"])
    higher = st.selectbox("Wants Higher Education", ["yes", "no"])
    internet = st.selectbox("Internet Access at Home", ["yes", "no"])
    romantic = st.selectbox("In Romantic Relationship", ["yes", "no"])
with col6:
    famrel = st.slider("Family Relationship Quality", 1, 5, 4)
    freetime = st.slider("Free Time After School", 1, 5, 3)
    goout = st.slider("Going Out with Friends", 1, 5, 3)
    dalc = st.slider("Workday Alcohol Consumption", 1, 5, 1)
    walc = st.slider("Weekend Alcohol Consumption", 1, 5, 2)
    health = st.slider("Current Health Status", 1, 5, 4)

# --- Academic Info ---
st.subheader("Academic Records")
col7, col8, col9 = st.columns(3)
with col7:
    absences = st.number_input("Number of Absences", 0, 93, 5)
with col8:
    G1 = st.number_input("First Period Grade (G1)", 0, 20, 10)
with col9:
    G2 = st.number_input("Second Period Grade (G2)", 0, 20, 10)

# Combine all into a DataFrame

input_df = pd.DataFrame({
    'school': [school],
    'sex': [sex],
    'age': [age],
    'address': [address],
    'famsize': [famsize],
    'Pstatus': [pstatus],
    'Medu': [medu],
    'Fedu': [fedu],
    'Mjob': [mjob],
    'Fjob': [fjob],
    'reason': [reason],
    'guardian': [guardian],
    'traveltime': [traveltime],
    'studytime': [studytime],
    'failures': [failures],
    'schoolsup': [schoolsup],
    'famsup': [famsup],
    'paid': [paid],
    'activities': [activities],
    'nursery': [nursery],
    'higher': [higher],
    'internet': [internet],
    'romantic': [romantic],
    'famrel': [famrel],
    'freetime': [freetime],
    'goout': [goout],
    'Dalc': [dalc],
    'Walc': [walc],
    'health': [health],
    'absences': [absences],
    'G1': [G1],
    'G2': [G2]
})

st.write("### Input Summary")
st.dataframe(input_df)

# 🔮 Prediction Button

# if st.button("🔮 Predict Final Grade"):
#     preds = predict(input_df)
#     st.success(f"Predicted Final Grade (G3): **{preds[0]}**")
#     # Create a simple bar chart
#     df = {

#     }
#     st.bar_chart(df)


if st.button("🔮 Predict Final Grade"):
    preds = predict(input_df)
    st.metric(label="Predicted Final Grade (G3)", value=f"{int(preds[0])} / 20")



