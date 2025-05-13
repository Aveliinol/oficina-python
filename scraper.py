import requests
from bs4 import BeautifulSoup
import csv

# URL alvo
url = 'https://books.toscrape.com/'

res = requests.get(url)
res.encoding = 'UTF-8'

soup = BeautifulSoup(res.text, 'html.parser')

livros = soup.find_all('article', class_='product_pod')

with open('livros.csv', 'w', newline='', encoding='UTF-8') as csv_files:
     escritor = csv.writer(csv_files)
     escritor.writerow(['titulo', 'preco', 'link'])
     for livro in livros:
      titulo = livro.h3.a['title']
      link = livro.h3.a['href']
      preco = livro.find('p', class_='price_color').text
      link_completo = url + link
      escritor.writerow([titulo, preco, link_completo])