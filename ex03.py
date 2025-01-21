import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 03 #

Informe as regiões com maiores crescimentos de PIB per capita no século passado.

'''

# Acessando arquivo e convertendo para DataFrame
arquivo = pd.read_csv('gdp.csv', decimal=".")
df_pib = pd.DataFrame(arquivo)

# Tratando os dados
df_pib['Year'] = pd.to_datetime(df_pib['Year'], format='%d/%m/%Y')
df_pib['GDP_pp'] = df_pib['GDP_pp'].apply(lambda x: float(x.replace(',', '')))

# Filtrando dados para o século (1900-1999)
df_pib_sec_passado = pd.DataFrame(df_pib[(df_pib['Year'] >= '1900-01-01') & (df_pib['Year'] < '2000-01-01')])

# Agrupando por país
pib_por_regiao = df_pib_sec_passado.groupby('Region').agg(start_gdp=('GDP_pp', 'first'), end_gdp=('GDP_pp', 'last')).reset_index()

# Calculando crescimento
pib_por_regiao['crescimento'] = (pib_por_regiao['end_gdp'] - pib_por_regiao['start_gdp']) / pib_por_regiao['start_gdp']

# Ordenando por crescimento
pib_por_regiao = pib_por_regiao.sort_values(by='crescimento', ascending=False)

# Exibindo o resultado em forma de gráfico
plt.figure(figsize=(12, 6))
plt.bar(pib_por_regiao['Region'], pib_por_regiao['crescimento'], color='skyblue', width=0.4, align='center')
plt.xlabel('Regiões')
plt.ylabel('Taxa de Crescimento (%)')
plt.title('Crescimento do PIB per Capita por Região (1900-1999)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()