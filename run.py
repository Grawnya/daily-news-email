import requests
import website
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

media_content = website.BBC(URL, soup)
dataframe = media_content.news_dataframe()