# -*- coding: utf-8 -*-
"""app 03 - Graficos nativos: st.line_chart, st.bar_chart e st.area_chart.

Como rodar:
    streamlit run app_03_graficos.py
"""
import pandas as pd
import streamlit as st

st.title('Graficos Nativos')
st.write('O Streamlit gera graficos simples diretamente dos DataFrames.')

# Preparacao dos dados: total de pedidos e receita por mes
df = pd.read_csv('vendas.csv', sep=';')
df['mes'] = df['data_hora'].str[:7]

mensal = df.groupby('mes').agg(
    pedidos=('cliente_id', 'count'),
    receita=('valor_venda', 'sum'),
).sort_index()

left, right = st.columns(2)

with left:
    st.header('Pedidos por mes')
    st.line_chart(mensal['pedidos'])

with right:
    st.header('Receita por mes')
    st.area_chart(mensal['receita'])

st.header('Pedidos por mes (barras)')
st.bar_chart(mensal['pedidos'])

st.caption('Toda a logica e Python/pandas; a parte web fica por conta do Streamlit.')