import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site
url = 'https://pokemondb.net/pokedex/national'

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrando todos os elementos que contêm as informações dos Pokémon
pokemon_list = soup.find_all('div', class_='infocard')

# Listas para armazenar os dados
names = []
types = []
images = []

# Extraindo as informações de cada Pokémon
for pokemon in pokemon_list:
    name = pokemon.find('a', class_='ent-name').text
    type_list = pokemon.find_all('a', class_='itype')
    type_names = [t.text for t in type_list]
    image = pokemon.find('span', class_='img-fixed img-sprite')['data-src']

    names.append(name)
    types.append(', '.join(type_names))
    images.append(image)

# Criando o DataFrame
df = pd.DataFrame({
    'Name': names,
    'Type': types,
    'Image': images
})

# Exportando para CSV
df.to_csv('pokemon_data.csv', index=False)

print('Dados exportados para pokemon_data.csv')