# Dashboard Macroeconômico Brasil — Contexto do Projeto

## Objetivo
Dashboard interativo com indicadores macroeconômicos do Brasil, com planos de expansão para outros países.

## Repositório
https://github.com/Luizreiss/Dashboard-de-indicadores-macroecon-micos-do-Brasil

## Stack
- **Frontend/Dashboard:** Streamlit
- **Gráficos:** Plotly
- **Dados Brasil:** python-bcb (Banco Central), sidrapy (IBGE)
- **Deploy:** Streamlit Cloud (conectado ao GitHub)
- **Linguagem:** Python

## Fontes de Dados
- **BCB (Banco Central do Brasil):** Selic, IPCA, câmbio, dívida pública
  - Biblioteca: `python-bcb`, acessa via SGS (Sistema Gerenciador de Séries)
- **IBGE:** PIB, desemprego (PNAD), produção industrial
  - Biblioteca: `sidrapy`, acessa via API SIDRA

## Estrutura de Pastas
```
/
├── app.py                  # Entrada principal do Streamlit
├── data/
│   ├── __init__.py
│   ├── bcb.py              # Coleta dados do Banco Central
│   └── ibge.py             # Coleta dados do IBGE
├── components/
│   ├── __init__.py
│   └── charts.py           # Funções de visualização Plotly
├── CLAUDE.md               # Este arquivo
└── requirements.txt        # Dependências Python
```

## Indicadores Planejados (Fase 1 — Brasil)
- [ ] IPCA (inflação)
- [ ] Taxa Selic
- [ ] PIB
- [ ] Taxa de desemprego (PNAD)
- [ ] Câmbio (USD/BRL)
- [ ] Dívida pública

## Decisões Técnicas
- Streamlit escolhido por ser 100% Python (usuário tem familiaridade com Python)
- Dados carregados com cache (`@st.cache_data`) para não bater na API a cada refresh
- Foco inicial no Brasil, expansão para outros países em fases futuras

## Como rodar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Como subir alterações para o GitHub
```bash
git add .
git commit -m "descrição do que foi feito"
git push
```
