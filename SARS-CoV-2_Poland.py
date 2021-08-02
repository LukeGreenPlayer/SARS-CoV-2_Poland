from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1V9frAv2pZW3qes-yRzt27i4y6hKCFKtA-1uNfThLNfc'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="TEST!A1:E10").execute()
values = result.get('values', [])


TEST = [["02.08.2021", 1000],["03.08.2021", 2000],["04.08.2021", 3000]]

request = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="TEST!A1", valueInputOption="USER_ENTERED", body={"values":TEST}).execute()

print(request)