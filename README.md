# Salary Prediction Machine Learning API

Production-ready Machine Learning regression project for salary prediction,
served via **FastAPI** and containerized using **Docker**.

---

## 📌 Problem Statement
This project predicts employee salary based on multiple numerical features
such as experience, education level, and skill score using a regression model.

---

## 📊 Dataset
- Clean synthetic dataset
- No missing values
- Numerical features only
- Target variable: `salary`

---

## 🤖 Model
- Algorithm: **Linear Regression**
- Evaluation Metrics:
  - RMSE
  - R² Score

---

## 🧱 Project Structure
salary-prediction-ml-api/
│── app/
│ ├── main.py
│ ├── schemas.py
│ ├── model.py
│── model/
│ └── salary_model.pkl
│── Dockerfile
│── requirements.txt
│── README.md



---

## 🛠 Tech Stack
- Python
- Pandas, NumPy, Scikit-learn
- FastAPI
- Docker

---

## 🚀 API Endpoint

### Predict Salary
**POST** `/predict`

#### Request Body
```json
{
  "experience_years": 5,
  "education_level": 3,
  "skill_score": 85
}

Response
{
  "predicted_salary": 8500000
}

Run Locally
pip install -r requirements.txt
uvicorn app.main:app --reload

Run with Docker
docker build -t salary-api .
docker run -p 8000:8000 salary-api

Author
---

## 3️⃣ Commit perbaikan README
```powershell
git add README.md
git commit -m "Improve README formatting and project documentation"
git push
