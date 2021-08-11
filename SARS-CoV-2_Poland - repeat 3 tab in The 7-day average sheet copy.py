from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '13XYlxpZF5WA6vN9EH2OWZchPiRwQ9UDwMUzp2LI5GgU'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

# How execute this ??? for: https://docs.google.com/spreadsheets/d/13XYlxpZF5WA6vN9EH2OWZchPiRwQ9UDwMUzp2LI5GgU/edit#gid=1342243109 
    reqs = {'requests': [
    
        {'repeatCell': {
            'range': {
                'startRowIndex': 3,
                'endRowIndex': 15,
                'startColumnIndex': 1,
                'endColumnIndex': 2,
        },
    }},
]}   
 



