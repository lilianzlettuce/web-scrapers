import requests
from bs4 import BeautifulSoup

def scrape(url) :
    try :
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        table = soup.find(id='pokedex')

        if table is None :
            print('No table')
        else :
            print(table.string)
            print('extra test')

            allRows = table.find_all('tr')

            for row in allRows :
                try :
                    print(row.get_text())
                    print('total: ' + row.find(class_='cell-total').get_text())
                except :
                    print('nothing')
    except :
        print('oopsy daisies')

#URL = 'https://en.wikipedia.org/wiki/Web_scraping'
URL = 'https://pokemondb.net/pokedex/all'

scrape(URL)