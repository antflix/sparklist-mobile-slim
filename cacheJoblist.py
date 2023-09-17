import os
import time

from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define the duration in seconds for which the cache is valid
CACHE_DURATION = 3600  # 1 hour

# Path to store the cached job list
CACHE_PATH = os.path.join(os.getcwd(), 'static', 'cached_joblist.txt')

def fetch_and_cache_joblist():
    # Google Sheets API credentials
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SAMPLE_SPREADSHEET_ID = '1xtWhD6CZq8ZOT-feGO7temN0jFJEhC2WPPE-8CcH0mQ'
    SAMPLE_RANGE_NAME = 'Building Blok Imported Active-Joblist!B1:B1000'
    secret_file = os.path.join(os.getcwd(), 'static', 'client_secrets.json')

    creds = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    try:
        # Call the Sheets API to get the data from the spreadsheet
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
        data = result.get('values', [])

        if not data:
            print("No data found.")
        else:
            # Generate the job list as a comma-separated string
            job_list = ','.join(row[0] for row in data)
            
            # Store the job list in a cached file
            with open(CACHE_PATH, 'w') as cache_file:
                cache_file.write(job_list)
    except Exception as error:
        print(f"An error occurred: {error}")

# Fetch and cache the job list initially and then at regular intervals
fetch_and_cache_joblist()
while True:
    time.sleep(CACHE_DURATION)
    fetch_and_cache_joblist()