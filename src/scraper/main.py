import requests
from bs4 import BeautifulSoup

url='https://news.ycombinator.com/'
response= requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')    
    title_elements = soup.find_all('span', class_='titleline')
    
    print("Titles of Hacker News: \n")
    for i, element in enumerate(title_elements, start=1):
        title = element.get_text(strip=True)
        print(f"{i}. {title}")
else:
    print(f"Error al acceder a la página: {response.status_code}")