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

#Unindo as duas bases de dados
df_total = pd.concat([df_mulheres, df_homens])

#Desenvolvendo o Dashboard

#Titulo para base de dados completa
st.title("Base de Dados")
st.header("Base de dados completa")
st.write(df_total)

#Mostrar a contagem geral de deputados
st.header('Contagem de deputados por estado')
contagem = df_total['siglaUf'].value_counts()
st.write(contagem)

#Titulo para base de dados filtrada
st.header("Base de dados - filtro por sexo")

#criando o selectbox para selecionar o sexo
opcao_sexo = st.selectbox('Selecione o sexo', df_total['Sexo'].unique())

#mostrar o dataframe com o filtro selecionado
df_filtrado_sexo = df_total[df_total['Sexo'] == opcao_sexo]
st.header('Deputados do sexo' + opcao_sexo)
st.write(df_filtrado_sexo)

#Mostrar contagem do dataframe filtrado
contagem_sexo = df_filtrado_sexo['Sexo'].value_counts()
st.write(df_contagem_sexo)

#mostrar o dataframe por estado a partir do que foi filtrado por sexo
opcao_estado = st.selectbox('Selecione o estado', df_filtrado_sexo['siglaUf'].unique())

#mostrar o dataframe com o filtro selecionado
df_filtrado_estado = df_filtrado_sexo[df_filtrado_sexo['siglaUf'] == opcao_estado]
st.header('Deputados do estado' + opcao_estado)
st.write(df_filtrado_estado)

#Agregando os dados por UF e Sexo
df_total_agregado = df_total.groupby(['siglaUf', 'Sexo'])['id'].count().reset_index()
df_total_agregado = df_total_agregado.rename(columns={'siglaUf': 'UF','id': 'Contagem'})

#Título para base de dados por Estado e Sexo
st.header("Base de dados agregada por Estado e por Sexo")
st.write(df_total_agregado)

#Criando gráfico de barras
fig_barras = px.bar(
    df_total_agregado,
    x='UF',
    y='Contagem',
    color='Sexo',
    labels={'UF': 'Unidade Federativa', 'Contagem': 'Quantidade'},
    barmode='group', #Gráfico de barras
    title='Quantidade de Deputados por UF e Sexo (barras)')

fig_barras_empilhadas = px.bar(
    df_total_agregado,
    x='UF',
    y='Contagem',
    color='Sexo',
    labels={'UF': 'Unidade Federativa', 'Contagem': 'Quantidade'},
    barmode='stack', #Gráfico de barras empilhadas
    title='Quantidade de Deputados por UF e Sexo (barras empilhadas)')

#Exibindo o gráfico no Streamlit
st.title("Exibições gráficas")
st.header("Gráfico de barras")
st.plotly_chart(fig_barras)
st.plotly_chart(fig_barras_empilhadas)

st.title("Utilizando o select box para que o usuário possa escolher um determinado Estado")

#Selectbox para seleção do estado
#Primeiro fazemos a lista de opções. 
#O unique() é utilizado para mostrar as ocorrências únicas de uma determinada coluna.

opcoes = df_total_agregado['UF'].unique()

estados_selecionados = st.multiselect("Selecione os estados que deseja visualizar:", opcoes, default=opcoes[:3])

#NOVIDADE: como estamos usando mais de um estado, não usamos o ==, mas a função ".isin"

df_filtrado = df_total_agregado[df_total_agregado['UF'].isin(estados_selecionados)]

#Agora criamos o gráfico de barras empilhadas
fig_barras_apos_selecao = px.bar(
    df_filtrado,
    x='UF',
    y='Contagem',
    color='Sexo',
    labels={'UF': 'Unidade Federativa', 'Contagem': 'Quantidade'},
    barmode='group', 
    title=f'Quantidade de Deputados por Sexo nos Estados {estados_selecionados}')
    #Aqui colocamos o estado_selecionado como um parâmetro, que é o definido na caixa de seleção

st.plotly_chart(fig_barras_apos_selecao)
