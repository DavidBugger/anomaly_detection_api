from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Load service account credentials
credentials = service_account.Credentials.from_service_account_file(
    'service_account_key.json',
    scopes=['https://www.googleapis.com/auth/cloud-identity']
)

# Request an access token
credentials.refresh(Request())
print("Access Token:", credentials.token)
