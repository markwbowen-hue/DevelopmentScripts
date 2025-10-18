import os
import requests
from msal import ConfidentialClientApplication

# Environment variables from GitHub Secrets
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://markbowire.sharepoint.com/.default"]  # Important for SharePoint REST API

# Acquire token using MSAL
app = ConfidentialClientApplication(APP_ID, authority=AUTHORITY, client_credential=APP_SECRET)
token = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in token:
    raise Exception(f"Token acquisition failed: {token}")

access_token = token["access_token"]

# SharePoint REST API endpoint
tenant_hostname = "markbowire.sharepoint.com"  # Replace with your actual tenant domain
url = f"https://markbowire.sharepoint.com/_api/SPSiteManager/Create"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json;odata=verbose",
    "Content-Type": "application/json;odata=verbose"
}

# Payload for creating a modern team site
payload = {
    "request": {
        "Title": "Project Alpha",
        "Url": f"https://markbowire.sharepoint.com/sites/projectalpha",
        "Lcid": 1033,
        "ShareByEmailEnabled": False,
        "WebTemplate": "GROUP#0",  # GROUP#0 = Modern Team Site with M365 Group
        "SiteDesignId": "00000000-0000-0000-0000-000000000000",
        "Owner": "admin@markbowire.onmicrosoft.com"  # Replace with your admin email
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code, response.json())
