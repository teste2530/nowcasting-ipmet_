
import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime

URL_RADAR = "https://www.ipmetradar.com.br/img-ppi/ppi-anim.gif"

st.set_page_config(
    page_title="Nowcasting IPMet",
    page_icon="🌧️",
    layout="wide"
)

st.title("🌧️ Nowcasting de Precipitação")
st.subheader("Radar meteorológico IPMet/UNESP — Bauru")

st.info(
    "Sistema experimental. Nesta etapa, estamos verificando "
    "o acesso à animação pública do radar."
)

@st.cache_data(ttl=300)
def obter_radar():
    resposta = requests.get(
        URL_RADAR,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    resposta.raise_for_status()

    conteudo = resposta.content
    imagem = Image.open(BytesIO(conteudo))

    quantidade_quadros = getattr(imagem, "n_frames", 1)

    return conteudo, quantidade_quadros, len(conteudo)

if st.button("🔄 Consultar radar agora"):
    obter_radar.clear()

try:
    conteudo, quantidade, tamanho = obter_radar()

    col1, col2, col3 = st.columns(3)
    col1.metric("Conexão", "Acessível")
    col2.metric("Quadros no GIF", quantidade)
    col3.metric("Tamanho do arquivo", f"{tamanho / 1024:.1f} KB")

    st.success("A animação foi baixada com sucesso.")

    imagem = Image.open(BytesIO(conteudo))
    imagem.seek(0)
    quadro = imagem.convert("RGB")

    st.subheader("Radar meteorológico")
    st.image(quadro, caption="Primeiro quadro da animação pública")

    st.caption(
        "Horário da consulta: "
        + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

    st.subheader("Próxima etapa")
    st.write(
        "Verificar os horários dos quadros e a possibilidade de "
        "extrair uma sequência adequada para estimar o deslocamento "
        "da precipitação."
    )

except Exception as erro:
    st.error("Não foi possível obter a animação do radar.")
    st.write(f"Detalhe técnico: {erro}")
    st.write(
        "O site pode estar indisponível ou impedir o acesso automático. "
        "Isso não significa necessariamente que o radar esteja fora do ar."
    )

st.divider()
st.caption(
    "Fonte: IPMet/UNESP — Bauru. "
    "Esta versão ainda não calcula previsões meteorológicas."
)
