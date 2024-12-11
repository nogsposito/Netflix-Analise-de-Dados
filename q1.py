# proporção filmes e séries no dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/clean_netflix_titles.csv')

data['type'] = data['type'].replace({'Movie': 'Filmes', 'TV Show': 'Séries'})

count_types = data['type'].value_counts()

count_types.plot(kind = 'bar', color = ['blue', 'green'])

plt.title('Proporção: Filmes x Séries')

plt.ylabel('Quantidade')
plt.xlabel('Tipo de mídia')

plt.show()