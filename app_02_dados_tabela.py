# -*- coding: utf-8 -*-
"""app 02 - Explorando dados na pagina: st.dataframe, st.table e estatisticas.

Como rodar:
    streamlit run app_02_dados_tabela.py
"""
import pandas as pd
import streamlit as st

st.title('Explorando os Dados')
st.caption('Comparando diferentes formas de exibir tabelas e estatisticas.')

df = pd.read_csv('vendas.csv', sep=';')

st.header('1. st.dataframe (interativo)')
st.write('Permite rolar, ordenar por coluna e escolher o tamanho.')
st.dataframe(df)

st.header('2. st.table (estatico)')
st.write('Renderiza a tabela completa, sem interatividade. Bons para poucas linhas.')
st.table(df.head(5))

st.header('3. Estatisticas descritivas')
st.write('Podemos exibir o resultado de `df.describe()` normalmente:')
st.dataframe(df.describe())

st.header('4. Configurar a altura da tabela')
st.write('Passando `height`, limitamos a area visivel com rolagem interna.')
st.dataframe(df, height=220)