import requests
from bs4 import BeautifulSoup

url='https://news.ycombinator.com/'
response= requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title_elements = soup.find_all('tr', class_='athing')
    
    print("Hacker News entries:\n")
    for i, element in enumerate(title_elements, start=1):

        title_tag = element.find('span', class_='titleline')
        title = title_tag.get_text(strip=True) if title_tag else 'Titleless'

        next_row = element.find_next_sibling('tr')
        subtext = next_row.find('td', class_='subtext') if next_row else None

        score_tag = subtext.find('span', class_='score') if subtext else None
        score = score_tag.get_text(strip=True) if score_tag else 'Scoreless'

        comment_links = subtext.find_all('a') if subtext else []
        comments_text = comment_links[-1].get_text(strip=True) if comment_links else 'No comments'
        comments = comments_text if 'comment' in comments_text else '0 comments'

        print(f"{i}. {title} - {score} - {comments}")
else:
    print(f"Error al acceder a la página: {response.status_code}")