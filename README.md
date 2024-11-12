

# Anomaly Detection API

This project is an **Anomaly Detection API** built with **FastAPI** and deployed on **Google Cloud Platform (GCP)** using **App Engine**. It detects anomalies in login attempts, integrating with an Active Directory setup to enhance security.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Deployment](#deployment)
- [Usage](#usage)
- [License](#license)

---

### Overview

The Anomaly Detection API is designed to analyze login attempts for unusual activity, leveraging a trained Support Vector Machine (SVM) model. The API integrates with Google Cloud Identity and uses tokens to validate users and predict anomalies in real time.

### Features

- **Anomaly Detection**: Uses an SVM model to classify login attempts as normal or anomalous.
- **User Validation**: Authenticates login attempts using Google Cloud Identity.
- **Scalable Deployment**: Runs on Google Cloud Platform’s App Engine for auto-scaling and efficient resource management.

---

### Tech Stack

- **FastAPI**: High-performance web framework for building APIs.
- **Google Cloud Platform (GCP)**: Cloud infrastructure used for deployment.
- **App Engine**: Serverless environment for deploying web applications.
- **Python**: Core programming language for building the API.
- **Joblib**: Library for serializing the SVM model.

---

### Project Structure

```plaintext
anomaly_detection_project/
│
├── app/
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # FastAPI application setup
│   ├── models.py                 # Pydantic models for request validation
│   ├── routes.py                 # API routes for prediction and validation
│   ├── preprocess.py             # Preprocessing functions for user data
│   ├── svm_model.joblib          # Serialized SVM model
│
├── requirements.txt              # Python dependencies
├── app.yaml                      # Google App Engine configuration
└── README.md                     # Project documentation
```

---

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/anomaly_detection_project.git
   cd anomaly_detection_project
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**  
   Add your environment variables (e.g., API keys, tokens) to a `.env` file or directly in `app.yaml`.

5. **Run the Application Locally**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Test the API**  
   Use [Postman](https://www.postman.com/) or `curl` commands to test endpoints.

---

### Deployment

1. **Initialize Google Cloud SDK**

   ```bash
   gcloud init
   ```

2. **Set Up Project and Enable App Engine**

   ```bash
   gcloud projects create YOUR_PROJECT_ID --organization=YOUR_ORG_ID
   gcloud app create --region=YOUR_REGION
   ```

3. **Deploy to App Engine**

   ```bash
   gcloud app deploy
   ```

4. **Access the API**

   ```bash
   gcloud app browse
   ```

---

### Usage

1. **Login Workflow**:  
   The login workflow validates the user token, preprocesses the data, and calls the anomaly detection endpoint. Here’s an example using `curl`:

   ```bash
   curl -X POST "https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/predict/" \
   -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
   -H "Content-Type: application/json" \
   -d '{
         "username": "johndoe",
         "features": [0.5, 1.2, -0.3, 2.4, 5.1, 1.3]
       }'
   ```

2. **Endpoints**:
   - **`/validate-user/`**: Validates the user token.
   - **`/predict/`**: Analyzes the provided features for anomalies.

---

### License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.



python app/main.py
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Steps to deploy to google cloud 
Step 1: Create app.yaml

Create an app.yaml file in the root of your project. This file tells GCP how to configure and run your application.
Step 2: Prepare Your Project for Deployment
    1. Install Requirements: Ensure all dependencies are listed in requirements.txt. Use this command to generate a requirements.txt
    pip freeze > requirements.txt
    2. Test Locally 
    uvicorn app.main:app --reload

Step 3: Initialize Google Cloud SDK and App Engine
Install Google Cloud SDK if you haven’t already: Install SDK.

Initialize the SDK and log in:
1. Install Google Cloud SDK if you haven’t already: Install SDK
2. Initialize the SDK and login
    gcloud init
    gcloud auth login
3. Set the project ID
    gcloud config set project YOUR_PROJECT_ID
4. Enable App Engine API:
    gcloud services enable appengine.googleapis.com
5. Enable App Engine API:
    gcloud app create --region=YOUR_REGION
6. Deploy the Application
    gcloud app deploy app.yaml
7. After deployment, to run on browser
    gcloud  app browse 

gcloud projects add-iam-policy-binding eastern-archive-440910-i4 --member="serviceAccount:eastern-archive-440910-i4@appspot.gserviceaccount.com" --role="roles/storage.admin"

