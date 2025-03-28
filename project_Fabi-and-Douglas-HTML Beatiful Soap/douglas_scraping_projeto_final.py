# -*- coding: utf-8 -*-
"""douglas_scraping projeto final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I8G447T16EqPj8b3FlYCpzjc98skCqBn
"""

from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
html = urlopen("https://store.steampowered.com/tags/pt/Indie/")
bs = BeautifulSoup(html, 'html.parser')

linhas = bs.find_all('div',{'class':'tab_item_top_tags'})

rows = bs.find_all('a',{'class':'tab_item'})

nome = []
preço = []
for i in rows:
    row = i.find("a",{'class':'tab_item'})
    descrDiv = i.find("div",{'class':'tab_item_content'})
    descriptionTag = descrDiv.find("div",{'class':'tab_item_name'})
    description = descriptionTag.text
    nome.append(description)
#     print(description)

    priceDiv = i.find("div",{'class':'discount_final_price'})
    if priceDiv is not None:
        price = priceDiv.text
    else:
        price = '$'
#     print(price)
    preço.append(price)
    print(description)
    print(price)

categorias=[]
for i in linhas:
  categorias.append(i.text)
categorias

df = pd.DataFrame({'Nome do Jogo': nome , 'Preço': preço, 'Categorias': categorias})

df.head(10)