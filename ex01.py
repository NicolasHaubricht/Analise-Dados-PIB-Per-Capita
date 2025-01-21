import pandas as pd

'''

# Exercicio 01 #

Limpe o conjunto de dados, convertendo strings em datas ou float, quando necessário.

'''

# Acessando arquivo e convertendo para DataFrame
arquivo = pd.read_csv('gdp.csv', decimal=".")
df_pib = pd.DataFrame(arquivo)

# Tratando os dados
df_pib['Year'] = pd.to_datetime(df_pib['Year'], format='%d/%m/%Y')
df_pib['GDP_pp'] = df_pib['GDP_pp'].apply(lambda x: float(x.replace(',', '')))