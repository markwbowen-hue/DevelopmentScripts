# keepalive.ps1
# Connect to Azure using a Service Principal or Managed Identity
Connect-AzAccount -ServicePrincipal -Tenant $env:TENANT_ID -ApplicationId $env:APP_ID -Credential (ConvertTo-SecureString $env:APP_SECRET -AsPlainText -Force)

# Perform a harmless action to simulate activity
Get-AzSubscription | Out-Host
