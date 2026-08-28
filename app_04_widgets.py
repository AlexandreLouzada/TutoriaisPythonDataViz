# -*- coding: utf-8 -*-
"""app 04 - Widgets de entrada: filtros dinamicos no DataFrame.

Como rodar:
    streamlit run app_04_widgets.py

Cada widget devolve um valor que usamos para filtrar os dados.
Toda alteracao em um widget re-executa o script de cima a baixo.
"""
import pandas as pd
import streamlit as st

st.title('Filtros Interativos')
st.write('Use os controles ao lado e observe os dados se atualizando.')

df = pd.read_csv('vendas.csv', sep=';')

# st.sidebar: mesma interface, porém em painel lateral
estado = st.sidebar.selectbox(
    'Estado',
    options=['Todos'] + sorted(df['estado'].unique()),
)

categorias = st.sidebar.multiselect(
    'Categorias',
    options=sorted(df['categoria'].unique()),
    default=sorted(df['categoria'].unique()),
)

status = st.sidebar.selectbox(
    'Status',
    options=['Todos'] + sorted(df['status'].unique()),
)

# st.slider devolve um numero dentro do intervalo
valor_min, valor_max = st.sidebar.slider(
    'Faixa de valor da venda',
    min_value=0,
    max_value=int(df['valor_venda'].max()) + 50,
    value=(0, int(df['valor_venda'].max())),
    step=100,
)

# Aplicando os filtros sobre o DataFrame
filtro = df.copy()
if estado != 'Todos':
    filtro = filtro[filtro['estado'] == estado]
if categorias:
    filtro = filtro[filtro['categoria'].isin(categorias)]
if status != 'Todos':
    filtro = filtro[filtro['status'] == status]
filtro = filtro[(filtro['valor_venda'] >= valor_min) & (filtro['valor_venda'] <= valor_max)]

st.metric('Registros encontrados', len(filtro))
st.dataframe(filtro[['cliente_id', 'valor_venda', 'estado', 'categoria', 'status', 'data_hora']])