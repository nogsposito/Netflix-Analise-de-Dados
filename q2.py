# como distribuição de filmes e séries varia por ano de lançamento

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data/clean_netflix_titles.csv')