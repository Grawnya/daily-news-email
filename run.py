import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/"
page = requests.get(URL)

