from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import requests

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("campaigns-317204-c9d6f98922b5.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
ss = file.open("Reetik -work")  #open sheet
ws = ss.worksheet('Sheet73')#to open tab
n=2;



while(n < 59):
    try:
        api_key = "8000a2b5-6895-4c06-a59f-5659e12db758" 
        email_address = ws.cell(n, 1).value
        response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email_address},headers = {'Authorization': "Bearer " + api_key })
        status = response.json()['status']      
        if status == "valid":
            ws.update_cell(n, 2, "valid")
            print("email is valid")
        elif status == "invalid":
            ws.update_cell(n, 2, "invalid")
            print("email is invalid")
        else:
            ws.update_cell(n, 2, "unknnown")
            print("email was unknown")
    except Exception as e:
        print(e)
        
    n=n+1;
