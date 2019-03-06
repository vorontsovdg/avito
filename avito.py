import requests
from bs4 import BeautifulSoup

avito_url = 'http://www.avito.ru/barnaul/sobaki?p=1'

def make_url(page):
    return 'http://www.avito.ru/barnaul/sobaki?p=' + str(page)
    


def get_html(url):
    return requests.get(url).text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_string = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    page_num = page_string.split('?p')[1].split('=')[-1]
    return int(page_num)









def main():
    pageCount = get_total_pages(get_html(avito_url))
    #for i in range(1,pageCount +1):
    print(pageCount)






if __name__ == '__main__':
    main()