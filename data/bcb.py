import pandas as pd
from bcb import sgs
import streamlit as st

# Códigos SGS do Banco Central
SERIES = {
    "selic": 11,        # Taxa Selic
    "ipca": 433,        # IPCA mensal
    "cambio": 1,        # USD/BRL (PTAX venda)
    "divida_pib": 4503, # Dívida bruta do governo geral (% PIB)
}

@st.cache_data(ttl=3600)
def get_serie(nome: str, anos: int = 5) -> pd.DataFrame:
    codigo = SERIES[nome]
    inicio = pd.Timestamp.today() - pd.DateOffset(years=anos)
    df = sgs.get({nome: codigo}, start=inicio)
    df.index.name = "data"
    return df.reset_index()
