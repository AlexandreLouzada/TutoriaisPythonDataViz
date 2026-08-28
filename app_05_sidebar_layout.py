# -*- coding: utf-8 -*-
"""app 05 - Layout: sidebar, colunas, expander e abas.

Como rodar:
    streamlit run app_05_sidebar_layout.py

Organize a interface com containers no Streamlit:
    st.sidebar | st.columns | st.expander | st.tabs
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Layout', layout='wide')

st.title('Organizando a Interface')

df = pd.read_csv('vendas.csv', sep=';')
df['mes'] = df['data_hora'].str[:7]

# ---- Sidebar: controles ficam em painel lateral ----
st.sidebar.title('Filtros')
regioes = st.sidebar.multiselect(
    'Regioes',
    options=sorted(df['regiao'].unique()),
    default=sorted(df['regiao'].unique()),
)

filtro = df[df['regiao'].isin(regioes)]

# ---- Colunas: distribui conteudo na horizontal ----
col_metricas, col_grafico = st.columns([1, 2])

filtro_sul = df[df['regiao'] == 'Sul']
col_metricas.subheader('Destaques')
col_metricas.metric('Filtradas', len(filtro))
col_metricas.metric('Receita Sul', f"R$ {filtro_sul['valor_venda'].sum():,.0f}".replace(',', '.'))

mensal = filtro.groupby('mes')[['valor_venda']].sum().rename(columns={'valor_venda': 'receita'})
col_grafico.subheader('Receita por mes')
col_grafico.bar_chart(mensal)

# ---- Expander: conteudo recolhido sob demanda ----
st.subheader('Estatisticas do recorte')
with st.expander('Ver detalhes'):
    st.dataframe(filtro.describe())

# ---- Abas: muda a secao sem sair da pagina ----
st.subheader('Analises')
aba_geral, aba_categoria = st.tabs(['Por estado', 'Por categoria'])

with aba_geral:
    st.bar_chart(filtro.groupby('estado')[['valor_venda']].sum())

with aba_categoria:
    st.bar_chart(filtro.groupby('categoria')[['valor_venda']].sum())

st.caption('Os containers ajudam o usuario a navegar com clareza.')