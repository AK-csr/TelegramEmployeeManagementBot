import gspread
import sys

sys.path.append('../telegrambot')
from config import SHEET_ID
from google.oauth2.service_account import Credentials


def accessWorkerSheet():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes = scopes)
    client = gspread.authorize(creds)

    sheet_id = SHEET_ID
    workbook = client.open_by_key(sheet_id)
    sheet = workbook.worksheet("L1")
    return sheet