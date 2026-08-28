# -*- coding: utf-8 -*-
"""app 01 - Primeiro app: titulos e exibicao de texto e dados.

Como rodar (na pasta do arquivo):
    streamlit run app_01_primeiro_app.py
"""
import pandas as pd
import streamlit as st

# Titulos estruturam a pagina como cabecalhos de um documento
st.title('Meu Primeiro App')
st.header('Tema: Analise de Vendas')
st.write('Vamos usar o Streamlit para transformar dados em paginas interativas.')

# Leitura dos dados do curso
df = pd.read_csv('vendas.csv', sep=';')

# st.write recebe texto com formatacao simples (*negrito*, _italico_) ou objetos
st.write(f'Carregamos **{len(df)}** registros de vendas.')

st.subheader('Tabela de dados')
# st.dataframe renderiza o DataFrame com rolagem e ordenacao por coluna
st.dataframe(df)