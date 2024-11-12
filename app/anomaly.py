from fastapi import APIRouter, HTTPException
import joblib
import numpy as np

detect_anomaly = APIRouter()

# Load the model when the app starts
model = joblib.load("app/model/svm_model.joblib")
def detect_anomaly(features: list) -> dict:
    prediction = model.predict([features])
    anomaly_detected = bool(prediction[0])  # Assuming 1 for anomaly, 0 for normal
    return {"anomaly_detected": anomaly_detected}

