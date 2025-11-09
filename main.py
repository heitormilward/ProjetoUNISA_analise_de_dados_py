#importar biblioteca
import pandas as pd

#importar a base de dados
tabela_vendas = pd.read_excel('Vendas (1).xlsx')

#visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

#lojas com maior faturamento
melhores_lojas = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum().sort_values('Valor Final', ascending=[False])
print(melhores_lojas.head(10))
print('-'*50)

#dias com mais vendas
melhores_dias = tabela_vendas[['Data', 'Quantidade']].groupby('Data').sum().reset_index()\
.sort_values('Quantidade', ascending=[False])
print(melhores_dias.head(10))
print('-'*50)

#produtos menos vendido
produtos_piores = tabela_vendas[['Produto', 'Quantidade']].groupby('Produto').sum().reset_index()\
.sort_values(['Quantidade'], ascending=[True])
print(produtos_piores.head(10))
print('-'*50)

#produtos mais vendido
produtos_melhores = tabela_vendas[['Produto', 'Quantidade']].groupby('Produto').sum().reset_index()\
.sort_values(['Quantidade'], ascending=[False])
print(produtos_melhores.head(10))
print('-'*50)


