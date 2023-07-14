import requests
from bs4 import BeautifulSoup
import json

def frontpage():
    url = 'https://wabetainfo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        
        for element in soup.find_all('article'):
            article_id = element.get('id')
            time = element.find('time').get('datetime')
            os = element.select('header > div > a:nth-child(3)')[0].get_text()
            title = element.select('h3.entry-title')[0].get_text()
            link = element.find('a').get('href')
            summary = element.find('p').get_text()

            
            articles.append({
                'id': article_id,
                'time': time,
                'title': title,
                'link': link,
                'os': os,
                'summary': summary
              
            })
        
        articles_json = json.dumps(articles, indent=4)
        return articles_json
    else:
        print(f"Error: {response.status_code}")



def news_content(link):
    url = link
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        
        soup = BeautifulSoup(html, 'html.parser')
        p_tags = soup.find_all('p')

        for p_tag in p_tags:
         
         return ("\n"+p_tag.get_text())

     

    else:
        print(f"Error: {response.status_code}")


