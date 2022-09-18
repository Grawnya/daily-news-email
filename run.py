import requests
import website
import yagmail
from bs4 import BeautifulSoup
yag = yagmail.SMTP('dailynewsemail22@gmail.com', oauth2_file='creds.json')

URL = "https://www.bbc.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

media_content = website.BBC(URL, soup)
dataframe = media_content.news_dataframe()

user_email = input('put In your email below\n')

contents = [
    '<h2>Here\'s the daily news from BBC</h2>',
    dataframe
]

yag.send(to=user_email, subject='Test123', contents='test')