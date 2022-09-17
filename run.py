import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

media_content = soup.find_all('div', class_='media__content')

news_headings = []

for each in media_content:
    heading_text = each.find("h3").get_text()
    heading_text = heading_text.replace('\n', '')
    heading_text = heading_text.strip(' ')
    news_headings.append(heading_text)
print(news_headings)