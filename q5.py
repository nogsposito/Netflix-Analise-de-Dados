# distribuição das classificações do conteúdo

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/clean_netflix_titles.csv')

print(data['rating'].value_counts())