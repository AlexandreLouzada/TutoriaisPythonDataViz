# -*- coding: utf-8 -*-
"""app 08 - Cache: acelerando o recarregamento com st.cache_data.

Como rodar:
    streamlit run app_08_cache.py

A cada interacao o script roda de cima a baixo. Com o cache, funcoes
marcadas sao executadas apenas quando os argumentos mudam: na 2a vez
que um mesmo filtro e pedido, o resultado vem da memoria/do disco.
"""
import pandas as pd
import streamlit as st

st.title('Cache de Dados')
st.write('Observe a mensagem de "processando": ela so aparece quando o calculo e novo.')


@st.cache_data
def carregar_dados():
    """Leitura do CSV e processamento pesado (ocorre uma unica vez)."""
    df = pd.read_csv('vendas.csv', sep=';')
    df['mes'] = df['data_hora'].str[:7]
    return df


@st.cache_data
def filtrar(regiao, categoria, valor_min, valor_max):
    """Filtro + agrupamento. Recalcula somente se os parametros mudarem."""
    df = carregar_dados()
    filtro = df[(df['regiao'] == regiao) & (df['categoria'] == categoria)]
    filtro = filtro[(filtro['valor_venda'] >= valor_min) & (filtro['valor_venda'] <= valor_max)]

    mensal = filtro.groupby('mes')[['valor_venda']].sum().rename(columns={'valor_venda': 'receita'})
    print('>> processando filtro...')  # visivel no terminal ao rodar de verdade
    return mensal


st.sidebar.title('Parametros')
regiao = st.sidebar.selectbox('Regiao', sorted(carregar_dados()['regiao'].unique()))
categoria = st.sidebar.selectbox('Categoria', sorted(carregar_dados()['categoria'].unique()))
valor_min, valor_max = st.sidebar.slider(
    'Faixa de valor',
    min_value=0,
    max_value=int(carregar_dados()['valor_venda'].max()) + 50,
    value=(0, int(carregar_dados()['valor_venda'].max())),
    step=100,
)

mensal = filtrar(regiao, categoria, valor_min, valor_max)

st.subheader(f'Receita por mes - {regiao} / {categoria}')
st.bar_chart(mensal)

if st.button('Limpar cache'):
    st.cache_data.clear()
    st.rerun()