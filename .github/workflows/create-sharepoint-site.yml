name: Create SharePoint Site

on:
  workflow_dispatch: # Manual trigger
  schedule:
    - cron: '0 9 * * *' # Runs daily at 09:00 UTC

jobs:
  create-site:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Validate secrets
        run: |
          if [ -z "${{ secrets.APP_ID }}" ] || [ -z "${{ secrets.APP_SECRET }}" ] || [ -z "${{ secrets.TENANT_ID }}" ]; then
            echo "❌ Missing required secrets: APP_ID, APP_SECRET, TENANT_ID"
            exit 1
          fi
          echo "✅ Secrets are set."

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests msal

      - name: Run create_site.py
        env:
          APP_ID: ${{ secrets.APP_ID }}
          APP_SECRET: ${{ secrets.APP_SECRET }}
          TENANT_ID: ${{ secrets.TENANT_ID }}
        run: |
          python create_site.py
