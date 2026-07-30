import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Medical Insurance Cost Predictor")

age = st.number_input("Age", 18, 100)
bmi = st.number_input("BMI", 10.0, 50.0)
children = st.number_input("Children", 0, 10)

sex = st.selectbox("Sex", ["Male", "Female"])
smoker = st.selectbox("Smoker", ["Yes", "No"])

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# Encoding
sex_code = 1 if sex == "Male" else 0
smoker_code = 1 if smoker == "Yes" else 0

# One-hot region encoding
northeast = 1 if region == "northeast" else 0
northwest = 1 if region == "northwest" else 0
southeast = 1 if region == "southeast" else 0
southwest = 1 if region == "southwest" else 0


if st.button("Predict"):

    input_data = [[
        age,
        bmi,
        children,
        smoker_code,
        sex_code,
        northeast,
        northwest,
        southeast,
        southwest
    ]]

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Insurance Cost: ${prediction[0]:.2f}"
    )