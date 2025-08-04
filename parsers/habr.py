import requests
from bs4 import BeautifulSoup

def get_habr_news(keyword: str) -> list:
    url = f'https://habr.com/ru/search/?q={keyword}&target_type=posts&order=relevance'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for article in soup.find_all('article', class_='tm-articles-list__item'):
        title = article.find('h2', class_='tm-title').get_text(strip=True)
        link = 'https://habr.com' + article.find('a', class_='tm-title__link')['href']
        articles.append(f'* {title}*\n{link}')
        
    return articles[:5]