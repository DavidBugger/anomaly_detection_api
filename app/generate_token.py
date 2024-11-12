from google_auth_oauthlib.flow import InstalledAppFlow

# Specify the scopes needed for your API
scopes = ['https://www.googleapis.com/auth/cloud-identity']

# Initiate the OAuth 2.0 flow with client credentials
flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret_894643635353-vsrvuip8vvfoe3e12cnmi47rvflpvadm.apps.googleusercontent.com.json', scopes=scopes
)
credentials = flow.run_local_server(port=0)

# Get the access token
print("Access Token:", credentials.token)
