mport os
import requests
from msal import ConfidentialClientApplication

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(APP_ID, authority=AUTHORITY, client_credential=APP_SECRET)
token = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in token:
    raise Exception(f"Token acquisition failed: {token}")

access_token = token["access_token"]
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

# Replace with your actual tenant hostname
hostname = "markbowire.sharepoint.com"
url = f"https://graph.microsoft.com/v1.0/sites/{hostname}/sites"

payload = {
    "displayName": "Project Alpha",
    "description": "Site for Project Alpha team collaboration",
    "webTemplate": "STS#3",
    "siteCollection": {"hostname": hostname}
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code, response.json())
