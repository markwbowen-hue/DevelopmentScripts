import os
import requests
from msal import ConfidentialClientApplication
from datetime import datetime

# Environment variables
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
TENANT_ID = os.getenv("TENANT_ID")

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

# Acquire token
app = ConfidentialClientApplication(APP_ID, authority=AUTHORITY, client_credential=APP_SECRET)
token = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in token:
    print("❌ Token acquisition failed:", token)
    exit(1)

access_token = token["access_token"]

# Dynamic site name
site_name = f"Project-{datetime.now().strftime('%Y%m%d')}"
mail_nickname = site_name.lower().replace("-", "")

# Graph API endpoint
url = "https://graph.microsoft.com/v1.0/groups"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

payload = {
    "displayName": site_name,
    "description": f"SharePoint site for {site_name}",
    "groupTypes": ["Unified"],
    "mailEnabled": True,
    "mailNickname": mail_nickname,
    "securityEnabled": False
}

try:
    response = requests.post(url, headers=headers, json=payload)
    print(f"✅ Status Code: {response.status_code}")
    if response.status_code in [200, 201]:
        print("✅ Group created successfully! SharePoint site will be provisioned automatically.")
        print(response.json())
    else:
        print("❌ Error occurred:")
        print("Response Headers:", response.headers)
        print("Response Text:", response.text)
except requests.exceptions.RequestException as e:
    print("❌ Request failed:", str(e))
