import os
import requests
from msal import ConfidentialClientApplication

APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]  # Correct scope

app = ConfidentialClientApplication(APP_ID, authority=AUTHORITY, client_credential=APP_SECRET)
token = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in token:
    raise Exception(f"Token acquisition failed: {token}")

access_token = token["access_token"]

tenant_hostname = "markbowire.sharepoint.com"
url = f"https://{tenant_hostname}/_api/SPSiteManager/Create"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json;odata=verbose",
    "Content-Type": "application/json;odata=verbose"
}

payload = {
    "request": {
        "Title": "Project Alpha",
        "Url": f"https://{tenant_hostname}/sites/projectalpha",
        "Lcid": 1033,
        "ShareByEmailEnabled": False,
        "WebTemplate": "GROUP#0",
        "SiteDesignId": "00000000-0000-0000-0000-000000000000",
        "Owner": "admin@markbowire.onmicrosoft.com"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code, response.json())
