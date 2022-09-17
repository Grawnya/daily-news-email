import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

media_content = soup.find_all('div', class_='media__content')

news_headings = []
supporting_info = []
links = []

for each in media_content:
    # heading_text = each.find("h3").get_text()
    # heading_text = heading_text.replace('\n', '')
    # heading_text = heading_text.strip(' ')
    # news_headings.append(heading_text)
    link = each.find_next("a").get('href')
    link = link.replace('\n', '')
    link = link.strip(' ')
    if 'https' not in link:
        link = URL + link[1:]
    links.append(link)
    # try:
    #     secondary_text = each.find("p").get_text()
    # except:
    #     secondary_text = 'No supporting text supplied, access the link for more info'
    # secondary_text = secondary_text.replace('\n', '')
    # secondary_text = secondary_text.replace('"', '')
    # secondary_text = secondary_text.strip(' ')
    # supporting_info.append(secondary_text)
print(links)