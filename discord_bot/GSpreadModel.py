import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


class GSpreadSheet:
    async def getSheet(self):
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        self.credentials = Credentials.from_service_account_file(
            "testproject-376908-ac0ad633a018.json", scopes=scopes
        )
        self.spreadsheet_url = "https://docs.google.com/spreadsheets/d/17f_ORmmuEUb5jSKC7tpdaEGGJEFNvYADa55wo78HRm0/edit#gid=0"
        gc = gspread.authorize(self.credentials)
        spreadsheet = gc.open_by_url(self.spreadsheet_url)
        return spreadsheet

    async def write(self, spreadsheet, words):
        spreadsheet.sheet1.update_cell(1, 1, words)
        return words
