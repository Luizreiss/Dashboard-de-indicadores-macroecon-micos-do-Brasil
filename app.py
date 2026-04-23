import streamlit as st
from data.bcb import get_serie
from data.ibge import get_desemprego, get_pib
from components.charts import line_chart, bar_chart

st.set_page_config(
    page_title="Dashboard Macroeconômico Brasil",
    page_icon="🇧🇷",
    layout="wide",
)

st.title("Dashboard Macroeconômico — Brasil")
st.caption("Fontes: Banco Central do Brasil (BCB) e IBGE")

anos = st.sidebar.slider("Período (anos)", min_value=1, max_value=10, value=5)

st.sidebar.markdown("---")
st.sidebar.markdown("**Indicadores**")
show_ipca    = st.sidebar.checkbox("IPCA (Inflação)", value=True)
show_selic   = st.sidebar.checkbox("Taxa Selic", value=True)
show_cambio  = st.sidebar.checkbox("Câmbio USD/BRL", value=True)
show_divida  = st.sidebar.checkbox("Dívida Pública (% PIB)", value=False)
show_desemp  = st.sidebar.checkbox("Desemprego (PNAD)", value=True)
show_pib     = st.sidebar.checkbox("PIB (variação %)", value=True)

col1, col2 = st.columns(2)

if show_ipca:
    with col1:
        df = get_serie("ipca", anos)
        st.plotly_chart(
            line_chart(df, "data", "ipca", "IPCA — Inflação Mensal (%)", "%"),
            use_container_width=True,
        )

if show_selic:
    with col2:
        df = get_serie("selic", anos)
        st.plotly_chart(
            line_chart(df, "data", "selic", "Taxa Selic (% a.a.)", "% a.a."),
            use_container_width=True,
        )

col3, col4 = st.columns(2)

if show_cambio:
    with col3:
        df = get_serie("cambio", anos)
        st.plotly_chart(
            line_chart(df, "data", "cambio", "Câmbio — USD/BRL", "R$"),
            use_container_width=True,
        )

if show_divida:
    with col4:
        df = get_serie("divida_pib", anos)
        st.plotly_chart(
            line_chart(df, "data", "divida_pib", "Dívida Bruta do Governo (% PIB)", "% PIB"),
            use_container_width=True,
        )

col5, col6 = st.columns(2)

if show_desemp:
    with col5:
        df = get_desemprego()
        st.plotly_chart(
            bar_chart(df, "trimestre", "desemprego", "Taxa de Desemprego — PNAD (%)", "%"),
            use_container_width=True,
        )

if show_pib:
    with col6:
        df = get_pib()
        st.plotly_chart(
            bar_chart(df, "trimestre", "variacao_pib", "PIB — Variação anual (%)", "%"),
            use_container_width=True,
        )
