import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 04 #

Preecha os anos ausentes em cada país com uma estimativa, baseada na diferença entre o próximo registro e o anterior.

'''

# Acessando arquivo e convertendo para DataFrame
arquivo = pd.read_csv('gdp.csv', decimal=".")
df_pib = pd.DataFrame(arquivo)

# Tratando os dados
df_pib['Year'] = pd.to_datetime(df_pib['Year'], format='%d/%m/%Y')
df_pib['GDP_pp'] = df_pib['GDP_pp'].apply(lambda x: float(x.replace(',', '')))

# Preenchendo os anos ausentes com uma estimativa baseada na diferença entre o próximo registro e o anterior
df_pib['GDP_pp'].fillna(method='ffill', inplace=True)

# Adicionando coluna de décadas
df_pib['Decade'] = (df_pib['Year'].dt.year // 10) * 10

# Calculando PIB médio por década
df_pib_por_decada = df_pib.groupby('Decade')['GDP_pp'].mean().reset_index()

# Exibindo o resultado em forma de gráfico
plt.figure(figsize=(12, 6))
plt.bar(df_pib_por_decada['Decade'], df_pib_por_decada['GDP_pp'], color='skyblue', width=8)
plt.xlabel('Décadas')
plt.ylabel('PIB per Capita Médio')
plt.title('PIB per Capita Médio por Década')
plt.xticks(df_pib_por_decada['Decade'], rotation=45)
plt.tight_layout()
plt.show()