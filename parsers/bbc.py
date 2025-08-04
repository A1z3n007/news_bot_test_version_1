import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_bbc_news(query: str) -> list:
    url = f'https://www.bbc.com/search?q={query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news = []
    for article in soup.find_all('div', class_='sc-ec2d82d7-0 hPYtEv'):
        title = article.find('h2', class_='sc-9d830f2a-3 duBczH').get_text(strip=True)
        link = article.find('a', class_='sc-8a623a54-0 hMvGwj')['href']
        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link
        news.append(f'* {title}*\n{link}')
        
    return news[:5]