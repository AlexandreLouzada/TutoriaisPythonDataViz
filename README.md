# Análise de Dados e Dashboards com Python

Material didático completo para um **curso técnico de Inteligência Artificial e Ciência de Dados**, organizado como uma sequência de tutoriais práticos em Jupyter Notebook (em português), aplicativos de dashboard em Streamlit e arquivos de dados de apoio para os exercícios.

Tudo foi construído para ser executado de ponta a ponta: cada tutorial foi validado célula a célula e os apps do Streamlit foram testados em modo headless.

---

## O que você vai aprender

- Fundamentos de pandas: leitura de CSV, limpeza, agregações e análise de dados
- Visualização de dados com Matplotlib e Seaborn
- Mapas interativos com Folium
- Requisições HTTP e captura de dados da web (web scraping)
- Computação numérica vetorizada com NumPy
- Bancos de dados relacionais com SQLAlchemy (SQL puro, Core e ORM)
- Aplicações web de dados com Streamlit (do primeiro app ao dashboard completo)

---

## Estrutura do repositório

```
/
├── *.ipynb                  # Tutoriais em Jupyter Notebook (pt-BR)
├── app_*.py                 # Apps Streamlit prontos para executar
├── *.csv                    # Dados de apoio usados nos tutoriais
└── README.md
```

### Tutoriais

| Tutorial | Células | Tópicos principais |
|----------|---------|--------------------|
| `pandas_guia_completo.ipynb` | 99 | Leitura de `vendas.csv`, limpeza (NaNs), tipos, agregações, `groupby`, merges, datas, exportação |
| `matplotlib_tutorial.ipynb` | 66 | Linhas, barras, histogramas, boxplot, pizza, subplots, formatação de eixos e legendas |
| `seaborn_tutorial.ipynb` | 62 | `relplot`, `catplot`, `distplot`, `heatmap`, `pairplot`, `clustermap`, temas |
| `folium_tutorial.ipynb` | 43 | Marcadores, `CircleMarker`, *popups*, `FeatureGroup`, `Choropleth` por região |
| `requests_tutorial.ipynb` | 52 | Métodos HTTP, parâmetros, headers, APIs públicas, extração com BeautifulSoup, `robots.txt` |
| `numpy_tutorial.ipynb` | 50 | `ndarray`, indexação, operações vetorizadas `ufunc`, agregações `nan*` |
| `sqlalchemy_tutorial.ipynb` | 46 | `engine`/`text()`, parâmetros seguros, Core (`Table`, `select`, `insert`, `update`), ORM (`mapped_column`, sessões, relacionamentos) |
| `streamlit_tutorial.ipynb` | 24 | Conceitos de Streamlit com explicação dos 9 apps do repositório |

### Apps Streamlit (`app_*.py`)

Rode qualquer app com: `streamlit run app_XX_nome.py`

| App | Tema |
|-----|------|
| `app_01_primeiro_app.py` | Títulos, `st.write`, primeira tabela |
| `app_02_dados_tabela.py` | `st.dataframe` vs `st.table`, estatísticas descritivas |
| `app_03_graficos.py` | Gráficos nativos: `st.line_chart`, `st.bar_chart`, `st.area_chart` |
| `app_04_widgets.py` | Filtros interativos: `selectbox`, `multiselect`, `slider` |
| `app_05_sidebar_layout.py` | Sidebar, colunas, `expander` e abas |
| `app_06_metricas_form.py` | `st.metric`, `st.progress`, formulário, `download_button`, `session_state` |
| `app_07_pyplot_matplotlib.py` | Gráficos do Matplotlib dentro do app (`st.pyplot`) |
| `app_08_cache.py` | Acelerando recargas com `st.cache_data` |
| `app_09_dashboard.py` | Dashboard completo de vendas (projeto final) |

### Dados de apoio

| Arquivo | Conteúdo |
|---------|----------|
| `vendas.csv` | 20 registros de vendas: `cliente_id`, `valor`, `valor_venda`, `estado`, `regiao`, `categoria`, `data_hora`, `email`, `status` e outros |
| `vendas_semestre1.csv` | Recorte do 1º semestre |
| `vendas_semestre2.csv` | Recorte do 2º semestre |
| `vendas_mensal.csv` | Vendas agregadas por mês |
| `clientes.csv` | Cadastro de clientes (para merges e relatórios) |
| `cidades.csv` | 15 capitais brasileiras (usado no Folium e em mapas) |
| `df1.csv` / `df2.csv` | Dados de exemplo para demonstrações de `merge` |

---

## Como usar

### 1. Instalação

Python 3.13+ recomendado.

```bash
python -m pip install jupyter pandas matplotlib seaborn folium requests beautifulsoup4 lxml numpy sqlalchemy streamlit scipy pyarrow
```

### 2. Execute os tutoriais

No terminal, dentro da pasta do projeto:

```bash
jupyter notebook
```

Abra o notebook desejado e rode as células em ordem. **As células de setup reiniciam os dados** (ex.: o `sqlalchemy_tutorial.ipynb` apaga o `loja.db` antes de criar o banco), então execute o notebook de cima para baixo.

### 3. Rode os apps Streamlit

```bash
streamlit run app_09_dashboard.py
```

Todos os apps usam o `vendas.csv` da mesma pasta. O `streamlit_tutorial.ipynb` explica cada um deles e como publicar no Streamlit Community Cloud.

---

## Sobre os dados (vendas.csv)

| Coluna | Descrição |
|--------|-----------|
| `cliente_id` | Identificador do cliente |
| `valor` | Valor com valores ausentes (exemplo de limpeza com `nan`) |
| `valor_venda` | Valor completo, usado para receita/ticket |
| `estado` | UF (SP, RJ, MG, SC, RS, BA, PE, PR) |
| `regiao` | Sudeste, Sul, Nordeste |
| `categoria` | Alimentos, Automotivo, Eletronicos, Livros, Moveis, Roupas |
| `data_hora` | Data/hora da venda (2024-01 a 2024-06) |
| `status` | Concluído, Pendente, Em andamento, Cancelado |

---

## Detalhes técnicos

- **Idioma:** todos os tutoriais estão em português (pt-BR).
- **Convenção:** cada tutorial é dividido em 3 níveis (Básico, Intermediário, Avançado) e termina com uma tabela-resumo de referência.
- **Validação:** todos os notebooks foram validados com execução de todas as células de código; os apps Streamlit foram testados com o `AppTest` (headless), sem exceções.
- **Ambiente testado:** Python 3.13, pandas 3.x, matplotlib 3.10.8, seaborn 0.13.2, folium 0.20.0, requests 2.33.1, beautifulsoup4, lxml, numpy 2.4.4, sqlalchemy 2.0.49, streamlit 1.57.0.