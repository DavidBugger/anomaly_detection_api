from fastapi import FastAPI, HTTPException
from app.models import LoginFeatures
from app.anomaly import detect_anomaly  # Ensure this handles the model prediction
from app.auth import validate_user
from app.login_workflow import login_workflow  # For integration testing
from google_auth_oauthlib.flow import InstalledAppFlow
app = FastAPI()
# Include routes from the `auth` and `anomaly` modules
app.include_router(validate_user)
# app.include_router(detect_anomaly)

@app.post("/predict/")
async def predict(features: LoginFeatures):
    try:
        # Preprocess the input features
        processed_features = features.preprocess()
        # Call the prediction function (ensure `detect_anomaly` uses the processed input)
        result = detect_anomaly(processed_features)
        return {"anomaly_detected": result["anomaly_detected"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add route for login workflow testing (optional)
@app.post("/login-flow/")
async def login_flow_endpoint(user_data: LoginFeatures, token: str):
    try:
        login_workflow(user_data.dict(), token)
        return {"message": "Login workflow executed successfully. Check server logs for details."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# @app.post('/generate_access_token')
# async def generate_access_token(self):
#     try:
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
