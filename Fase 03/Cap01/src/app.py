import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from clima_api import obter_dados_climaticos
from conexao import OracleDB
from data.crud_cultura import listar_culturas_com_area
from data.crud_adubacao import listar_adubacoes
from data.crud_fungicida import listar_fungicidas

# 🎨 Estilo CSS externo
st.set_page_config(page_title="Dashboard Agrícola", page_icon="🌾",  layout="centered",initial_sidebar_state='collapsed')

with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Função auxiliar
def obter_leituras_por_area(cursor, cd_area):
    cursor.execute("""
        SELECT s.tp_sensor, l.dt_leitura, l.vl_valor
        FROM Leitura_Sensor l
        JOIN Sensor s ON s.cd_sensor = l.cd_sensor
        WHERE s.cd_area = :1
        ORDER BY l.dt_leitura DESC
    """, (cd_area,))
    return cursor.fetchall()

st.title("🌱 Dashboard de Monitoramento Agrícola")

try:
    db = OracleDB()
    cursor = db.cursor

    culturas = listar_culturas_com_area(cursor)
    if not culturas:
        st.warning("Nenhuma cultura cadastrada.")
    else:
        cultura_opcoes = {
    f"{c[1].capitalize()} - Área {c[9]} ({c[3]} ha)": c for c in culturas}
        cultura_selecionada = st.selectbox("Selecione a cultura / área:", list(cultura_opcoes.keys()))
        cultura_dados = cultura_opcoes[cultura_selecionada]
        cd_area = cultura_dados[9]

        # 🌤️ Clima
        temperatura, umidade, precipitacao, condicao = obter_dados_climaticos()
        st.markdown("## 🌤️ Clima Atual (Jundiaí)")
        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperatura (°C)", f"{temperatura:.1f}")
        col2.metric("💧 Umidade (%)", f"{umidade:.0f}")
        col3.metric("🌧️ Precipitação (mm)", f"{precipitacao:.1f}")
        st.caption(f"Condição: {condicao.capitalize()}")
        if umidade < 65:
            st.error("🚨 Irrigação recomendada (umidade abaixo de 65%)")
        else:
            st.success("✅ Umidade adequada")

        st.markdown("---")

        # 📊 Leituras lado a lado
        st.markdown("## 📊 Leituras de Sensores")
        leituras = obter_leituras_por_area(cursor, cd_area)
        if leituras:
            df = pd.DataFrame(leituras, columns=["Tipo", "Data", "Valor"])
            df["Data"] = pd.to_datetime(df["Data"])

            tipos = df["Tipo"].unique()
            colunas = st.columns(len(tipos))

            for idx, tipo in enumerate(tipos):
                df_tipo = df[df["Tipo"] == tipo]
                with colunas[idx]:
                    st.markdown(f"#### {tipo.capitalize()}")
                    fig, ax = plt.subplots(figsize=(4, 3))
                    ax.plot(df_tipo["Data"], df_tipo["Valor"], marker="o", linewidth=1)
                    ax.set_xticks(df_tipo["Data"][::max(1, len(df_tipo)//4)])
                    ax.tick_params(axis='x', rotation=45)
                    ax.set_xlabel("")
                    ax.set_ylabel("Valor")
                    ax.grid(True)
                    st.pyplot(fig)
        else:
            st.warning("Nenhuma leitura registrada.")

        st.markdown("---")

        # 🧪 Aplicações
        st.markdown("## 🧪 Aplicações")
        adubacoes = [a for a in listar_adubacoes(cursor) if a[6] == cd_area]
        fungicidas = [f for f in listar_fungicidas(cursor) if f[4] == cd_area]

        if adubacoes:
            st.markdown("### 🌾 Adubação")
            df_adubo = pd.DataFrame(adubacoes, columns=["Código", "Data", "Total", "Área", "P", "K", "N"])
            st.dataframe(df_adubo[["Data", "Total", "P", "K", "N"]], use_container_width=True)
        else:
            st.info("Nenhuma adubação registrada.")

        if fungicidas:
            st.markdown("### 🛡️ Fungicida")
            df_fun = pd.DataFrame(fungicidas, columns=["Código", "Data", "Total", "Nome", "Área"])
            st.dataframe(df_fun[["Data", "Nome", "Total"]], use_container_width=True)
        else:
            st.info("Nenhuma aplicação de fungicida registrada.")

except Exception as e:
    st.error("Erro ao carregar dados do banco. Verifique a conexão.")
    import traceback
    st.text(traceback.format_exc())
finally:
    if 'db' in locals():
        db.fechar()
