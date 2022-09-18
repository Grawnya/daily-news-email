import requests
import website
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

media_content = website.WebsiteInformation(URL, soup, 'div', 'media__content', 'h3', 'p', 'a')
# headings = media_content.headings()
# secondary = media_content.secondary_info()
# links = media_content.links()
links = media_content.news_dataframe()