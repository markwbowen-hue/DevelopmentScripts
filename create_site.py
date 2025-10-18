import os
import requests
from msal import ConfidentialClientApplication
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
token = app.acquire_token_for_client(scopes=SCOPE)

access_token = token.get("access_token")
headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}

url = "https://graph.microsoft.com/v1.0/sites/contoso.sharepoint.com/sites"
payload = {
    "displayName": "Project Alpha",
    "description": "Site for Project Alpha team collaboration",
    "webTemplate": "STS#3",
    "siteCollection": {"hostname": "MARKBOWIRE.sharepoint.com"}
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code, response.json())
