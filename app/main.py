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
    age: int
    projects_count: int
    certification_count: int
    overtime_hours: float


@app.post("/predict")
def predict_salary(data: SalaryInput):

    if not (0 <= data.skill_score <= 100):
        raise ValueError("skill_score harus 0–100")

    if data.experience_years < 0:
        raise ValueError("experience_years tidak valid")

    X = [[
        data.experience_years,
    data.education_level,
    data.skill_score,
    data.age,
    data.projects_count,
    data.certification_count,
    data.overtime_hours
    ]]
    X_scaled = scaler.transform(X)
    salary = model.predict(X_scaled)[0]


    return {"predicted_salary": int(salary)}
