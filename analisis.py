# importação de bibliotecas: pandas, maplot,pyplot e seaborn
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# função do pandas para ler dataset csv
data = pd.read_csv('netflix_titles.csv')

# verificando se tudo está correto:
print(data.head())
print(data.info())
print(data.describe())

# printando a quantidade de valores nulos por coluna
print(data.isnull().sum())