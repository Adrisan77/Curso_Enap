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
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#retirar o Unnamed
df.drop(columns=['Unnamed: 0'], inplace=True)

#converter as colunas Lat_d e Long_d para valores numéricos
list= ['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
df.info()

#criar o selectbox com os Estados
#para criar o selectbox precisamos primeiro criar um dataframe com o lista dos Estados
#criar dataframe com o nome estados
#para não repetir os nomes, inserimos a função "unique"
estados = df['NM_UF'].unique()

#criar uma variável para armazenar o estado selecionado a partir do selectbox
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)

#mostrar o dado selecionado
st.write('Você selecionou: ', estadoFiltro)

#criar um novo dataframe que mostre apenas os dados do estado selecionado
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]

#inserir checkbox para marcar "Mostrar tabela"
if st.checkbox('Mostrar tabela') ==True:
  st.write(dadosFiltrados)

#criar o mapa a partir dos dados filtrados
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")

#exibir a quantidade de municípios no Estado selecionado usando a função len(), que mede a quantidade de linhas de um dataframe
#usamos o "unique", que informa quantas ocorrências únicas existe em uma coluna

qtdeMunicipios = len(dadosFiltrados['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(dadosFiltrados['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

#Usando a função nativa do streamlit para fazer bar_chart
st.header("Número de comunidades por UF - usando o bar-chart")
st.bar_chart(df['NM_UF'].value_counts())
