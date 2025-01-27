#Bibliotecas

import requests
import pandas as pd
import plotly.express as px
import streamlit as st

st.warning('Para entender o passo a passo, consulte também o caderno collab "Adriana_Exercícios_Aula10_Encerramento"')

#Manipulação da base de dados - mulheres
url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta_mulheres = requests.get(url_mulheres)
dadosJSONmulheres = resposta_mulheres.json()
df_mulheres = pd.DataFrame(dadosJSONmulheres['dados'])
df_mulheres['Sexo'] = "Feminino"

#Manipulação da base de dados - homens
url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta_homens = requests.get(url_homens)
dadosJSONhomens = resposta_homens.json()
df_homens = pd.DataFrame(dadosJSONhomens['dados'])
df_homens['Sexo'] = "Masculino"

#Desenvolvendo o Dashboard

#Unindo as duas bases de dados
df_total = pd.concat([df_mulheres, df_homens])

#titulo para base de dados completa
st.title("Base de Dados")
st.header("Base de Dados Completa")
st.write(df_total)

#agregando os dados por UF e Sexo
df_total_agregado = df_total.groupby(['siglaUf', 'Sexo'])['id'].count().reset_index()
df_total_agregado = df_total_agregado.rename(columns={'siglaUf': 'UF',
                                                      'id': 'Contagem'})

#título para base de dados por Estado e Sexo
st.header("Base de dados agregada por Estado e por Sexo")
st.write(df_total_agregado)

#criando gráfico de barras empilhadas
fig_barras = px.bar(
    df_total_agregado,
    x='UF',
    y='Contagem',
    color='Sexo',
    labels={'UF': 'Unidade Federativa', 'Contagem': 'Quantidade'},
    barmode='group', #Gráfico de barras
    title='Quantidade de Deputados por UF e Sexo (barras)'
)

fig_barras_empilhadas = px.bar(
    df_total_agregado,
    x='UF',
    y='Contagem',
    color='Sexo',
    labels={'UF': 'Unidade Federativa', 'Contagem': 'Quantidade'},
    barmode='stack', #Gráfico de barras empilhadas
    title='Quantidade de Deputados por UF e Sexo (barras empilhadas)'
)
