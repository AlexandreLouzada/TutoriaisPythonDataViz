# -*- coding: utf-8 -*-
"""app 09 - Dashboard completo de vendas (projeto final do tutorial).

Como rodar:
    streamlit run app_09_dashboard.py

Reune tudo: sidebar com filtros, metricas, abas com graficos nativos,
tabela detalhada e botao de download.
"""
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Dashboard de Vendas', layout='wide')

st.title('Dashboard de Vendas')
st.caption('Painel unificado com os recursos vistos nos apps anteriores.')


@st.cache_data
def carregar_dados():
    df = pd.read_csv('vendas.csv', sep=';')
    df['mes'] = df['data_hora'].str[:7]
    return df


df = carregar_dados()

# ---------------- Sidebar: filtros globais ----------------
st.sidebar.title('Filtros')

regioes = st.sidebar.multiselect(
    'Regioes',
    options=sorted(df['regiao'].unique()),
    default=sorted(df['regiao'].unique()),
)

categorias = st.sidebar.multiselect(
    'Categorias',
    options=sorted(df['categoria'].unique()),
    default=sorted(df['categoria'].unique()),
)

status = st.sidebar.selectbox('Status', ['Todos'] + sorted(df['status'].unique()))

valor_min, valor_max = st.sidebar.slider(
    'Faixa de valor da venda',
    min_value=0,
    max_value=int(df['valor_venda'].max()) + 50,
    value=(0, int(df['valor_venda'].max())),
    step=100,
)

freq = st.sidebar.radio('Periodo', ['Mensal', 'Trimestral'])

# ---------------- Aplicacao dos filtros ----------------
filtro = df[df['regiao'].isin(regioes) & df['categoria'].isin(categorias)]
if status != 'Todos':
    filtro = filtro[filtro['status'] == status]
filtro = filtro[(filtro['valor_venda'] >= valor_min) & (filtro['valor_venda'] <= valor_max)]

if freq == 'Trimestral':
    filtro['periodo'] = filtro['mes'].apply(lambda m: f"{m[:4]}-T{(int(m[5:7]) - 1) // 3 + 1}")
else:
    filtro['periodo'] = filtro['mes']

# ---------------- Metricas principais ----------------
col1, col2, col3, col4 = st.columns(4)
col1.metric('Receita total', f"R$ {filtro['valor_venda'].sum():,.0f}".replace(',', '.'))
col2.metric('Numero de pedidos', len(filtro))
col3.metric('Ticket medio', f"R$ {filtro['valor_venda'].mean():,.2f}".replace(',', '.'))
col4.metric('Estados atendidos', filtro['estado'].nunique())

st.divider()

# ---------------- Abas de analise ----------------
aba_mensal, aba_categoria, aba_estado, aba_dados = st.tabs(
    ['Evolucao', 'Categorias', 'Estados', 'Dados detalhados']
)

with aba_mensal:
    receita_periodo = filtro.groupby('periodo')[['valor_venda']].sum().rename(
        columns={'valor_venda': 'receita'})
    pedidos_periodo = filtro.groupby('periodo')[['cliente_id']].count().rename(
        columns={'cliente_id': 'pedidos'})
    serie = receita_periodo.join(pedidos_periodo)
    st.line_chart(serie)

with aba_categoria:
    st.bar_chart(filtro.groupby('categoria')[['valor_venda']].sum().sort_values('valor_venda'))

with aba_estado:
    st.bar_chart(filtro.groupby('estado')[['valor_venda']].sum().sort_values('valor_venda'))

with aba_dados:
    st.dataframe(filtro[['cliente_id', 'valor_venda', 'estado', 'regiao',
                         'categoria', 'status', 'data_hora']])
    st.download_button(
        label='Baixar dados filtrados (CSV)',
        data=filtro.to_csv(index=False).encode('utf-8'),
        file_name='dashboard_vendas.csv',
        mime='text/csv',
    )

st.divider()
st.caption('Fim do dashboard. Modifique os filtros e veja tudo reagir em tempo real.')