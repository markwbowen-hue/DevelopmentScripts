# Convert secret to PSCredential
$securePassword = ConvertTo-SecureString $env:APP_SECRET -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($env:APP_ID, $securePassword)

# Authenticate
Connect-AzAccount -ServicePrincipal -Tenant $env:TENANT_ID -Credential $credential

# Harmless activity
Get-AzSubscription | Out-Host
