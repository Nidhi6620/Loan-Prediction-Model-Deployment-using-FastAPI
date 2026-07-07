from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the trained model
model = joblib.load("loan_model.joblib")


# Input schema
class LoanRequest(BaseModel):
    Age: int
    Salary: int


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Loan Prediction API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict(data: LoanRequest):

    input_data = [[data.Age, data.Salary]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Not Approved"

    return {
        "Prediction": result
    }