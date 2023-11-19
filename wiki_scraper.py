import requests
from bs4 import BeautifulSoup
import random

def scrape(url, num, backupLinks) :
    if num > 0 :
        try :
            page = requests.get(url)

            num -= 1 

            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id='firstHeading')

            if title is None :
                scrape(getLink(backupLinks), num, backupLinks)
            else :
                print(iteration - num, ' ', title.string)

                allLinks = soup.find(id='bodyContent').find_all('a')
                scrape(getLink(allLinks), num, allLinks)
        except :
            scrape(getLink(backupLinks), num, backupLinks)

def getLink(links) :
    random.shuffle(links)
    linkEl = None

    for link in links : 
        #print('href: ', link['href'])
        try :
            if link['href'].find('/wiki/') != -1 : 
                linkEl = link
                break
        except : 
            break
    
    linkToScrape = 'https://en.wikipedia.org' + linkEl['href'] 
    return linkToScrape

#URL = 'https://en.wikipedia.org/wiki/Web_scraping'
#URL = 'https://en.wikipedia.org/wiki/Death'
URL = 'https://en.wikipedia.org/wiki/Pope_Francis'
#URL = 'https://en.wikipedia.org/wiki/Special:Random'
iteration = 10

scrape(URL, iteration, None)