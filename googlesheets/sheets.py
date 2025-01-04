import gspread
from google.oauth2.service_account import Credentials


def accessWorkerSheet():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("../credentials.json", scopes = scopes)
    client = gspread.authorize(creds)

    sheet_id = "1z4rT4uU4p3c5GwS9PqlZlGbc43bzEdRlteZR6jEHk-A"
    workbook = client.open_by_key(sheet_id)
    sheet = workbook.worksheet("L1")
    return sheet