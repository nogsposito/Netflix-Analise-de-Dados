# quantidade de filmes e séries adicionados à netflix por ano

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/clean_netflix_titles.csv')

count_lancamento = data['release_year'].value_counts().sort_index()

count_lancamento.plot(kind='line')

plt.title('Distribuição de filmes e séries por ano de lançamento')
plt.ylabel('Quantidade')
plt.xlabel('Ano')

plt.show()