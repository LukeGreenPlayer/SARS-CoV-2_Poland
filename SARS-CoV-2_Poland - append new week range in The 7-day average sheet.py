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


data = [["200", "198","223","196","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")',"","15.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!D2")',"06.09.2021"],
        
        ["198", "223","196","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")',"","16.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!D2")',"07.09.2021"],
        
        ["223", "196","0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")',"","17.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!D2")',"08.09.2021"],
        
        ["196", "0","0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")',"","18.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!D2")',"09.09.2021"],
        
        ["0", "0",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B2")','',"19.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!D2")',"10.09.2021"],
        
        ["0", '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B2")',"","20.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!D2")',"11.09.2021"],
        
        ['=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!B2")', '=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 2!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 3!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 4!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 5!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 6!B2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7!B2")',"","21.08.2021","","","",'=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 1!H2")','=IMPORTRANGE("https://docs.google.com/spreadsheets/d/1_iDGD9XEd5Lw_AvmVo3XkAa4rBstaemnHeLKpyTgt8g", "Dzień 7!D2")',"12.09.2021"]]

request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range="Średnia 7 dni SARS-CoV-2!A1:G1", valueInputOption="USER_ENTERED",
                               insertDataOption="INSERT_ROWS", body={"values":data}).execute()
                                                 
print(request)
