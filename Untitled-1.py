import pandas as pd

#importando os dados
df1 = pd.read_csv("dataset_grupo1.csv", encoding="latin1", sep = ";")

df2 = pd.read_csv("dataset2_grupo1.csv", encoding="latin1", sep = ";")

df3 = pd.read_csv("dataset3_grupo1.csv", encoding="latin1", sep = ";")

#fazendo a junção dos dados em uma tabela única
dados = pd.merge(df1, df2, on="Data")
dados = pd.merge(dados, df3, on="Data")

dados.head()
 
 #conferindo os dados:
print(dados.isnull().sum())
#não há n.a values
print(dados['Data'].value_counts().sort_index())
# dados não repetidos
print(dados.nunique())

#aparentemente tudo certo :)
