import requests
from bs4 import BeautifulSoup as bs
def parse_ranobelib(name):

    params = {'name' : 'Гурман из другого мира'}

    response = requests.get('https://ranobelib.me/manga-list', params = params)
    soup = bs(response.text, 'html.parser')

    url = soup.find_all('a', class_ ="media-card")[0].get('href')

    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    name = soup.find_all('div', class_ = "media-name__main")[0].text
    chapter_amount = soup.find_all('div', class_="media-info-list__value text-capitalize")[1].text
    chapter_url = soup.find_all('a', class_ ="button button_block button_primary")[0].get('href')
    # for x in range():

    # return name


print(parse_ranobelib('https://ranobelib.me/gourmet-of-another-world?section=info'))