import sidrapy
import pandas as pd
import streamlit as st

@st.cache_data(ttl=3600)
def get_desemprego() -> pd.DataFrame:
    # Tabela 6381 — PNAD Contínua, taxa de desocupação trimestral
    data = sidrapy.get_table(
        table_code="6381",
        territorial_level="1",
        ibge_territorial_code="all",
        variable="4099",
        period="last 20",
    )
    df = pd.DataFrame(data[1:], columns=data[0])
    df = df[["D3C", "V"]].rename(columns={"D3C": "trimestre", "V": "desemprego"})
    df["desemprego"] = pd.to_numeric(df["desemprego"], errors="coerce")
    return df.dropna()

@st.cache_data(ttl=3600)
def get_pib() -> pd.DataFrame:
    # Tabela 1621 — PIB trimestral (variação % em relação ao mesmo período do ano anterior)
    data = sidrapy.get_table(
        table_code="1621",
        territorial_level="1",
        ibge_territorial_code="all",
        variable="583",
        period="last 20",
    )
    df = pd.DataFrame(data[1:], columns=data[0])
    df = df[["D3C", "V"]].rename(columns={"D3C": "trimestre", "V": "variacao_pib"})
    df["variacao_pib"] = pd.to_numeric(df["variacao_pib"], errors="coerce")
    return df.dropna()
