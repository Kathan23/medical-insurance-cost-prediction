# Import dependencies
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import pickle


from schema.user_input import UserInput

# Load the ML model
with open("model/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI
app = FastAPI(title="Insurance Premium Prediction API")

@app.get("/")
def home():
    return {"Message" : "This is the home page of Medical Insurance cost prediction API"}

@app.get("/health")
def health_check():
    return {"Message" : "ok"}

# API Endpoint for Prediction
@app.post("/predict")
def predict_insurance(data: UserInput):
    # Convert input into a dataframe for model
    input_df = pd.DataFrame(
        [
            {
                "Age": data.Age,
                "Diabetes": int(data.Diabetes),
                "BloodPressureProblems": int(data.BloodPressureProblems),
                "AnyTransplants": int(data.AnyTransplants),
                "AnyChronicDiseases": int(data.AnyChronicDiseases),
                "Height": data.Height,
                "Weight": data.Weight,
                "KnownAllergies": int(data.KnownAllergies),
                "HistoryOfCancerInFamily": int(data.HistoryOfCancerInFamily),
                "NumberOfMajorSurgeries": data.NumberOfMajorSurgeries,
                "bmi": data.bmi,
            }
        ]
    )

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Return as JSON
    return JSONResponse(
        status_code=200, content={"predicted_insurance": float(prediction)}
    )
