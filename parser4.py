from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

import requests

def get_html(url):
    html = requests.get(url)
    return html.text

def get_ad(html):
    soup = BeautifulSoup(html, "html.parser")
    ads = soup.find('div', class_='snippet-list js-catalog_serp')#.findAll('div', class_='snippet-horizontal   item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended')
    #print(ads)
    for ad in ads:
        try:
            url = 'https://www.avito.ru'+ad.find('a', class_='snippet-link').get('href')
            print(url)
            
        except:
            print('None')
def main():
    for i in range(1,2):
        a = 'p='
        base_url = 'https://www.avito.ru/moskva_i_mo/avtomobili/bmw?'   #генерируем ссылку на страницу
        url = base_url + a + str(i)
        #print(url)
        get_html(url)
    html = get_html(url)
    get_ad(html)

if __name__ == '__main__':
    main()


    #findAll('div', class_='snippet-list js-catalog_serp').