# -*- coding: utf-8 -*-
"""app 06 - Metricas, formularios, download e estado da sessao.

Como rodar:
    streamlit run app_06_metricas_form.py
"""
import pandas as pd
import streamlit as st

st.title('Metricas, Formularios e Download')

df = pd.read_csv('vendas.csv', sep=';')

# ---- st.metric: indicador com valor e variacao ----
col1, col2, col3 = st.columns(3)
col1.metric('Receita total', f"R$ {df['valor_venda'].sum():,.0f}".replace(',', '.'))
col2.metric('Pedidos', len(df))
col3.metric('Ticket medio', f"R$ {df['valor_venda'].mean():,.2f}".replace(',', '.'))

# ---- st.progress: barra de progresso ----
percentual_concluidos = (df['status'] == 'Concluído').mean()
st.progress(float(percentual_concluidos))
st.write(f'Percentual de vendas concluidas: {percentual_concluidos:.0%}')

# ---- st.form: agrupa campos, o submit roda de uma vez ----
st.header('Cadastro rapido de cliente')

with st.form('form_cliente'):
    nome = st.text_input('Nome do cliente')
    uf = st.selectbox('UF', ['SP', 'RJ', 'MG', 'SC', 'RS', 'BA', 'PE', 'PR'])
    enviar = st.form_submit_button('Cadastrar')

if enviar and nome.strip():
    st.success(f'Cliente {nome} ({uf}) cadastrado com sucesso!')
elif enviar:
    st.warning('Informe um nome para cadastrar.')

# ---- st.session_state: lembra valores entre as reexecucoes ----
st.header('Contador com session_state')
if 'cliques' not in st.session_state:
    st.session_state['cliques'] = 0

if st.button('Clique aqui'):
    st.session_state['cliques'] += 1

st.write(f'Numero de cliques: {st.session_state["cliques"]}')

# ---- st.download_button: gera um arquivo para baixar ----
st.header('Baixar dados')
st.download_button(
    label='Baixar vendas em CSV',
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='vendas_filtradas.csv',
    mime='text/csv',
)