import requests
from bs4 import BeautifulSoup

def get_rbk_news(query: str) -> list:
    url = f'https://www.rbc.ru/search/?query={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news = []
    for article in soup.find_all('div', class_='search-item js-search-item '):
        title = article.find('span', class_='search-item__title ').get_text(strip=True)
        link = article.find('a', class_='search-item__link  js-search-item-link')['href']
        news.append(f'* {title}*\n{link}')
        
    return news[:5]