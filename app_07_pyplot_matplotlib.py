# -*- coding: utf-8 -*-
"""app 07 - Integrando Streamlit com os graficos do Matplotlib.

Como rodar:
    streamlit run app_07_pyplot_matplotlib.py

Com st.pyplot enviamos qualquer figura do Matplotlib para a pagina,
reaproveitando tudo que vimos no curso.
"""
import matplotlib

matplotlib.use('Agg')  # backend sem janela, ideal para apps web

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

st.title('Graficos com Matplotlib')

df = pd.read_csv('vendas.csv', sep=';')
df['mes'] = df['data_hora'].str[:7]

# Receita por estado
por_estado = df.groupby('estado')[['valor_venda']].sum().sort_values('valor_venda')

fig, ax = plt.subplots(figsize=(7, 4))
top = por_estado.tail(5)
ax.barh(top.index, top['valor_venda'])
ax.set_title('Top 5 estados por receita')
ax.set_xlabel('Receita (R$)')
ax.set_ylabel('Estado')
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Evolucao mensal da receita
mensal = df.groupby('mes')[['valor_venda']].sum()

fig2, ax2 = plt.subplots(figsize=(7, 4))
ax2.plot(mensal.index, mensal['valor_venda'], marker='o')
ax2.set_title('Evolucao mensal da receita')
ax2.set_xlabel('Mes')
ax2.set_ylabel('Receita (R$)')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig2)
plt.close(fig2)

st.caption('Combine a biblioteca de graficos que preferir com st.pyplot.')