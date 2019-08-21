# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:35:02 2019

@author: Paulo Franco
"""
import pandas as pd
from periodos_dia import periodo

# Dataset de vendas
sales = pd.read_csv("data/arquivo-full.csv",delimiter=',',error_bad_lines=False,encoding='ISO-8859-1')

# Eliminando registros que sem dia e hora definida
sales.dropna(subset=['dateTime'],inplace=True)

# convertendo para formato de data
sales['dateTime'] = sales['dateTime'].apply(lambda x: x  if pd.isnull(x) else pd.to_datetime(x,errors='coerce'))

#Criação de campos de hora e período
sales['hora'] = sales['dateTime'].apply(lambda x: x  if pd.isnull(x) else pd.to_datetime(x,errors='coerce').strftime("%H"))
sales['periodo'] = sales['hora'].apply(lambda x: periodo(int(x)).get('id'))

#Eliminando os itens cujo id da venda não é numérico
sales = sales[sales.encrypted_saleid.str.isnumeric() == True]

#Dataset de lojas
stores = pd.read_csv("data/stores.csv",delimiter=',',error_bad_lines=False,encoding='ISO-8859-1')
stores.encrypted_5_zipcode.fillna(0,inplace=True)
stores.cnae.fillna(0,inplace=True)


# Agrupamento dos datasets de lojas e respectivas vendas
data_linx = pd.merge(sales, stores, on='encrypted_cnpj')

#Agrupamento baseado na descrição do produto
grupo_prod = sales.groupby(['prod_fullname']).count()

#Agrupamento baseado em vendas
grupo_venda = sales.groupby(['encrypted_saleid']).count()

# vendas agrupadas por cnpj
vendas_cpf = sales.dropna(subset=['encrypted_buyer_cpf'])

# vendas agrupadas por cpf
vendas_pj = sales.dropna(subset=['encrypted_buyer_cnpj'])

# vendas por cnpj por venda
grp_vendas_pj = vendas_pj.groupby(['encrypted_saleid']).count()

# vendas por cpf por venda
grp_vendas_cpf = vendas_cpf.groupby(['encrypted_saleid']).count()

#
qtd_vendas_cnpj = sales.groupby(['encrypted_cnpj']).count()

#
qtd_vendas_cpf = sales.groupby(['encrypted_buyer_cpf']).count()
qtd_vendas_pj = sales.groupby(['encrypted_buyer_cnpj']).count()

