
import streamlit as st

st.set_page_config(
    page_title="Nowcasting IPMet",
    page_icon="🌧️",
    layout="wide"
)
st.title("🌧️ Nowcasting de Precipitação")
st.subheader("Radar meteorológico IPMet/UNESP — Bauru")
st.info(
    "Sistema experimental em desenvolvimento. "
    "A conexão com os dados reais do radar ainda será implementada."
)
col1, col2, col3 = st.columns(3)
col1.metric("Radar", "A conectar")
col2.metric("Previsão", "Em desenvolvimento")
col3.metric("Última atualização", "—")
st.divider()
st.subheader("Monitoramento da chuva")
st.write(
    "Nesta área serão exibidos os dados de refletividade "
    "do radar e a previsão de deslocamento da precipitação."
)
st.subheader("Previsões futuras")
col1, col2, col3, col4 = st.columns(4)
col1.metric("15 minutos", "Aguardando dados")
col2.metric("30 minutos", "Aguardando dados")
col3.metric("45 minutos", "Aguardando dados")
col4.metric("60 minutos", "Aguardando dados")
