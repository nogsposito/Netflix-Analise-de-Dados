# distribuição da duração dos filmes

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/clean_netflix_titles.csv')

filmes = data[data['type'] == 'Movie']
print(filmes['duration'].value_counts().head(20))