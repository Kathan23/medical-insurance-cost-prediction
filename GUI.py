import streamlit as st
import requests

API_URL = 'http://backend:8000/predict'


st.title("Medical Insurance Cost Predictor")

st.markdown('Enter your details below')

# Inputs 

Age = st.number_input("Age", min_value=1,max_value=120,value=20)
Diabetes = st.selectbox("Do you have Diabetes?", options=[True,False])
BloodPressureProblems = st.selectbox("Do you have Blood Pressure Problem?", options=[True,False])
AnyTransplants = st.selectbox("Did you have any transplant?", options=[True,False])
AnyChronicDiseases = st.selectbox("Do you have any Chronic Diseases?", options=[True,False])
Height = st.number_input("Height (m)",value= 1.7)
Weight = st.number_input("Weight (kg)", value= 70.0)
KnownAllergies = st.selectbox("Do you have any Allergies?", options=[True,False])
HistoryOfCancerInFamily = st.selectbox("Does your family has cancer history?", options=[True,False])
NumberOfMajorSurgeries = st.selectbox("Number of major surgeries",[0,1,2,3])

if st.button("Predict Medical Insurance"):
    input_data = {
        "Age" : Age,
        "Diabetes" : int(Diabetes),
        "BloodPressureProblems" : int(BloodPressureProblems),
        "AnyTransplants" :int(AnyTransplants),
        'AnyChronicDiseases' : int(AnyChronicDiseases),
        "Height" : Height,
        "Weight" : Weight,
        "KnownAllergies" : int(KnownAllergies),
        "HistoryOfCancerInFamily" : int(HistoryOfCancerInFamily),
        "NumberOfMajorSurgeries" : NumberOfMajorSurgeries

    }

    # Send request to FastAPI server
    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium: **{result['predicted_insurance']}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running on port 8000.")