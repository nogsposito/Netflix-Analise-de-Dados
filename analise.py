# importação de bibliotecas: pandas, maplot,pyplot e seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# função do pandas para ler dataset csv
data = pd.read_csv('data/netflix_titles.csv')

# verificando se tudo está correto:
print("\n --- Verificações Iniciais --- \n")
print(data.head())
print(data.info())
print(data.describe()) # analisa distribuição das variáveis, fornecendo média, etc.

# removendo linhas duplicadas, aplicada diretamente no datas
data.drop_duplicates(inplace = True)

# printa total de valores nulos e remove linhas com valores nulos:
print("\n --- Verificação e Remoção de nulos --- \n")
print(data.isnull().sum())
data = data.dropna()
print(data.isnull().sum()) # demonstrando que todos os valores nulos foram removidos

# exemplo de exploração de filme por ano:
print(data['release_year'].value_counts().head(10))

# exemplo de demonstração gráfica com seaborn e pyplot (filmes por ano de lançamento)
sns.histplot(data['release_year'], kde = True)
plt.title('Distribuição de filmes por anos de lançamento')
plt.show()

# leva os dados limpos para um novo arquivo para as questões:
data.to_csv('data/clean_netflix_titles.csv', index = False)