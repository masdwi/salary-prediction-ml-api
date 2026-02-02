from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

app = FastAPI()

# Load model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model_gaji_ridge.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler_gaji.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

class SalaryInput(BaseModel):
    experience_years: float
    education_level: int
    skill_score: float

@app.post("/predict")
def predict_salary(data: SalaryInput):
    if data.skill_score < 0 or data.skill_score > 100:
        raise ValueError("skill_score tidak valid")

    X = scaler.transform([[data.experience_years, data.education_level, data.skill_score]])
    salary = model.predict(X)[0]

    return {"predicted_salary": int(salary)}
