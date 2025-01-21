import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''

# Exercicio 02 #

Você conseguiria informar o primeiro valor registrado de cada país?

'''

# Acessando arquivo e convertendo para DataFrame
arquivo = pd.read_csv('gdp.csv', decimal=".")
df_pib = pd.DataFrame(arquivo)

# Tratando os dados
df_pib['Year'] = pd.to_datetime(df_pib['Year'], format='%d/%m/%Y')
df_pib['GDP_pp'] = df_pib['GDP_pp'].apply(lambda x: float(x.replace(',', '')))

# Agrupando por país e pegando o primeiro valor registrado
resultado = df_pib.groupby('Country')['GDP_pp'].first()

# Exibindo o resultado em forma de gráfico
plt.figure(figsize=(12, 6))
plt.bar(resultado.index, resultado.values, width=0.4, align='center')
plt.xlabel('Países')
plt.ylabel('PIB per Capita')
plt.title('Primeiro valor de PIB per Capita de cada país')
plt.xticks(rotation=-45)
plt.tight_layout()
plt.show()