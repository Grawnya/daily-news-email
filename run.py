import requests
import website
import gspread
from google.oauth2.service_account import Credentials
from bs4 import BeautifulSoup

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('daily_news')

news_worksheet = SHEET.worksheet('news')
news_worksheet.clear()

URL = "https://www.bbc.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

media_content = website.BBC(URL, soup)
dataframe = media_content.news_dataframe()
news_worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
link_to_google_sheet = r'https://docs.google.com/spreadsheets/d/143icvVJJeDVEQsTzTy1y-brqLPJZwOX-WHkro4dN4lM/edit?usp=sharing'
print('To view the news headings, secondary info and links, click the link below:')
print(link_to_google_sheet)