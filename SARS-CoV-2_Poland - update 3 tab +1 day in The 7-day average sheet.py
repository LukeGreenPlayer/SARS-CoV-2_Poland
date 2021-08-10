from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '1D_ykOMbV2CdHMzLGT1nPZxpLEyyNEln8nhFIn5nwsQM'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dni - Zakres 2 tygodnie!B3").execute()
values = result.get('values', [])

RUN1 = [["={ 'Średnia 7 dni SARS-CoV-2'!H137 }", "={ 'Średnia 7 dni SARS-CoV-2'!I137 }"]]

request1 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dni - Zakres 2 tygodnie!B3", valueInputOption="USER_ENTERED", body={"values":RUN1}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Średnia 7 dni - Zakres 4 tygodnie!B3").execute()
values = result.get('values', [])

RUN2 = [["={ 'Średnia 7 dni SARS-CoV-2'!H122 }", "={ 'Średnia 7 dni SARS-CoV-2'!I122 }"]]

request2 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Średnia 7 dni - Zakres 4 tygodnie!B3", valueInputOption="USER_ENTERED", body={"values":RUN2}).execute()
                                                 

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Prognoza liczby zgonów - 21 dni do przodu!B3").execute()
values = result.get('values', [])

RUN3 = [["={ 'Średnia 7 dni SARS-CoV-2'!O129 }", "={ 'Średnia 7 dni SARS-CoV-2'!P129 }"]]

request3 = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                 range="Prognoza liczby zgonów - 21 dni do przodu!B3", valueInputOption="USER_ENTERED", body={"values":RUN3}).execute()                                                

print(request1, request2, request2)
