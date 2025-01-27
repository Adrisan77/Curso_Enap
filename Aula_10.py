#Bibliotecas

import requests
import pandas as pd
import plotly.express as px
import streamlit as st

st.warning('Para entender o passo a passo, consulte também o caderno collab "Adriana_Exercícios_Aula10_Encerramento"')

Manipulação da base de dados - mulheres
url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta_mulheres = requests.get(url_mulheres)
dadosJSONmulheres = resposta_mulheres.json()
df_mulheres = pd.DataFrame(dadosJSONmulheres['dados'])
df_mulheres['Sexo'] = "Feminino"

Manipulação da base de dados - homens
url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta_homens = requests.get(url_homens)
dadosJSONhomens = resposta_homens.json()
df_homens = pd.DataFrame(dadosJSONhomens['dados'])
df_homens['Sexo'] = "Masculino"

Unindo as bases de dados 
df_total = pd.concat([df_mulheres, df_homens])

Criando o Dashboard
st.title("Base de Dados")
st.header("Base de Dados Completa")
st.write(df_total)
