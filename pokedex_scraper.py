import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

import statistics
import re

def not_hidden(class_):
    # return class_ and not re.compile('hidden').search(class_)
    print(str(class_))
    if (class_ and 'hidden' in class_):
        return False
    else:
        return True

def no_class(tag):
    return not tag.has_attr('class')

def scrape(url, type) :
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(id='pokedex')

    if table is None :
        print('No table')
    else :
        print(type)

        allRows = table.find_all('tr')
        allTotals = []

        for row in allRows :
            try :
                #print(row.get_text())
                total = row.find(class_='cell-total').get_text()
                types = row.find(class_='cell-icon').get_text()
                if type in types:
                    allTotals.append(int(total))

                    #print('total: ' + total)
                    #print('types: ' + types)
            except :
                print('nothing')

        print('Number: ' + str(len(allTotals)))
        print('Mean: ' + str(statistics.mean(allTotals)))
        print('Median: ' + str(statistics.median(allTotals)))
        print('\n')

        return allTotals

URL = 'https://pokemondb.net/pokedex/all'
allTypes = ['Normal', 'Fire', 'Water', 'Electric', 'Grass',
            'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 
            'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 
            'Dark', 'Steel', 'Fairy']

for type in allTypes:
    data = scrape(URL, type)

    plt.style.use('_mpl-gallery')

    fig = plt.figure(figsize =(10, 7))
 
    # Creating plot
    plt.boxplot(data, vert=False,
                showmeans=True, showfliers=True,)
    
    # show plot
    plt.show()

