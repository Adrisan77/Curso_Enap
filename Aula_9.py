import streamlit as st
st.title("Questão 1")
st.write("Sou servidor público")

st.divider()
#1)importar as bibliotecas
import streamlit as st
import pandas as pd

#2) criar o dataframe
#criando o dataframe (o datafame possui duas colunas: nomeServidor e salario)
#veja que o dataframe é um dicionário de listas
df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]})

#3)exibir o título e a tabela com a base de dados
st.header("Base de dados")
st.write(df)

#4) criar a caixa de seleção com o nome das servidores
#utilizando o selectbox precisamos passar os dados: texto que o usuário irá se orientar e a indicar o coluna da tabela que ele terá que selecionar
#criamos uma nova variável (opcao) para armazenar o dado selecionado, assim podemos filtrar os dados com base na variável armazenada
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

#4.1) deixar a primeira opção de um st.selectbox em branco
# Adicionar uma opção em branco no início da lista
opcoes = [''] + list(df['nomeServidor'])

opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
    opcoes)

#5) inserir texto com o resultado da seleção
st.write('Você selecionou: ', opcao)

#6) criar novo dataframe exibindo apenas o que for selecionado na caixa de seleção
dadosFiltrados = df[df['nomeServidor'] == opcao]
st.write(dadosFiltrados)
