#1)importar as bibliotecas
import streamlit as st
import pandas as pd

#2)inserir o titulo do dashboard e subtítulo
st.title("Questão 1")
st.header("Sou servidor público")
st.divider()

#3) criar o dataframe
#criando o dataframe (o datafame possui duas colunas: nomeServidor e salario)
#veja que o dataframe é um dicionário de listas
df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]})

#4)exibir o subtítulo e a tabela com a base de dados
st.subheader("Base de dados")
st.write(df)

#5) criar a caixa de seleção com o nome das servidores
#utilizando o selectbox precisamos passar os dados: texto que o usuário irá se orientar e a indicar o coluna da tabela que ele terá que selecionar
#criamos uma nova variável (opcao) para armazenar o dado selecionado, assim podemos filtrar os dados com base na variável armazenada
selecao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])

#5.1) deixar a primeira opção de um st.selectbox em branco
# Adicionar uma opção em branco no início da lista
opcoes = [''] + list(df['nomeServidor'])

selecao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
    opcoes)

#6) inserir texto com o resultado da seleção
st.write('Você selecionou: ', selecao)

#7) criar novo dataframe exibindo apenas o que for selecionado na caixa de seleção
dadosFiltrados = df[df['nomeServidor'] == selecao]
st.write(dadosFiltrados)

#importar as bibliotecas
import streamlit as st
import pandas as pd

#inserir o número da questão
st.title("Questão 2")

#criar o titulo para o dashboard
st.header("Localização das comunidades quilombolas (2022)")
st.divider()

#carregar os dados
df = pd.read_csv('/content/BR_LQs_CD2022.csv')
df
