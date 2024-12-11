import pandas as pd

data = {'Nome': ['Alice', 'Bob', None, 'Vini'],
        'Idade': [25, None, None, 22],
        'Salario': [5000, 2400, None, 4500]}

df = pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum()) 