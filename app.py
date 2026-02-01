from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import logging

# =========================
# LOGGING (GLOBAL)
# =========================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model = joblib.load("model_gaji_ridge.pkl")
scaler = joblib.load("scaler_gaji.pkl")

app = FastAPI()

class EmployeeInput(BaseModel):
    umur: int
    pengalaman_kerja: int
    jam_kerja_per_minggu: int
    pendidikan: int
    skill_score: float
    lokasi_index: float
    performa: float

@app.post("/predict")
def predict_salary(data: EmployeeInput):

    # =========================
    # VALIDASI BISNIS (DI SINI)
    # =========================
    if data.skill_score < 0 or data.skill_score > 100:
        logger.warning("Invalid skill_score: %s", data.skill_score)
        raise HTTPException(
            status_code=400,
            detail="skill_score harus di antara 0 - 100"
        )

    logger.info("Request valid, mulai prediksi")

    df = pd.DataFrame([data.dict()])

    df_scaled = scaler.transform(df)
    prediction = model.predict(df_scaled)

    logger.info("Prediksi berhasil")

    return {
        "predicted_salary": int(prediction[0])
    }
