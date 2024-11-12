import requests

def login_workflow(user_data, auth_token):
    # Step 1: Validate user token
    validate_response = requests.get(
        'http://localhost:8000/validate-user/',
        headers={'Authorization': f'Bearer {auth_token}'}
    )
    if validate_response.status_code == 200:
        print("User token is valid. Proceeding to anomaly detection.")
        
        # Step 2: Anomaly detection
        anomaly_response = requests.post(
            'http://localhost:8000/predict/',
            json={"features": user_data["features"]}
        )
        
        if anomaly_response.status_code == 200:
            result = anomaly_response.json()
            if result["anomaly_detected"]:
                print("Anomaly detected during login attempt. Triggering security protocols.")
            else:
                print("No anomaly detected. Login successful.")
        else:
            print(f"Error during anomaly check: {anomaly_response.status_code}")
    else:
        print(f"Invalid user token: {validate_response.status_code}, {validate_response.text}")
