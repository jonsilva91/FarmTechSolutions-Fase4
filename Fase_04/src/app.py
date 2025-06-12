import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from clima_api import obter_dados_climaticos
from conexao import SQLiteDB
from data.crud_cultura import listar_culturas_com_area
from data.crud_adubacao import listar_adubacoes
from data.crud_fungicida import listar_fungicidas

# Configurações da página
st.set_page_config(
    page_title="Dashboard Agrícola",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state='collapsed'
)

# Carrega CSS externo
with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Função para obter leituras por área
def obter_leituras_por_area(cursor, cd_area):
    cursor.execute(
        """
        SELECT s.tp_sensor, l.dt_leitura, l.vl_valor
        FROM Leitura_Sensor l
        JOIN Sensor s ON s.cd_sensor = l.cd_sensor
        WHERE s.cd_area = ?
        ORDER BY l.dt_leitura DESC
        """,
        (cd_area,)
    )
    return cursor.fetchall()

# Título do dashboard
st.title("🌱 Dashboard de Monitoramento Agrícola")

try:
    with SQLiteDB() as db:
        cursor = db.cursor

        # Lista de culturas e áreas
        culturas = listar_culturas_com_area(cursor)
        if not culturas:
            st.warning("Nenhuma cultura cadastrada.")
            st.stop()

        # Mapeia opções para selectbox
        opcoes = [f"{c['nm_cultura'].capitalize()} - Área {c['cd_area']} ({c['vl_area_ha']} ha)" for c in culturas]
        escolha = st.selectbox("Selecione a cultura / área:", opcoes)
        sel = culturas[opcoes.index(escolha)]
        cd_area = sel['cd_area']

        # 🌤️ Clima Atual
        temperatura, umidade, precipitacao, condicao = obter_dados_climaticos()
        st.markdown("## 🌤️ Clima Atual (Jundiaí)")
        c1, c2, c3 = st.columns(3)
        c1.metric("🌡️ Temperatura (°C)", f"{temperatura:.1f}")
        c2.metric("💧 Umidade (%)", f"{umidade:.0f}")
        c3.metric("🌧️ Precipitação (mm)", f"{precipitacao:.1f}")
        st.caption(f"Condição: {condicao.capitalize()}")
        if umidade < 65:
            st.error("🚨 Irrigação recomendada (umidade abaixo de 65%)")
        else:
            st.success("✅ Umidade adequada")

        st.markdown("---")

        # 📊 Leituras de Sensores
        st.markdown("## 📊 Leituras de Sensores")
        leituras = obter_leituras_por_area(cursor, cd_area)
        if leituras:
            df = pd.DataFrame([dict(r) for r in leituras])
            df['dt_leitura'] = pd.to_datetime(df['dt_leitura'])
            df['tp_sensor'] = df['tp_sensor'].str.strip().str.lower()
            tipos = df['tp_sensor'].unique()
            cols = st.columns(len(tipos))
            for i, tipo in enumerate(tipos):
                df_t = df[df['tp_sensor'] == tipo]
                titulo = tipo.capitalize() if tipo not in ['ph','fosforo','potassio','nitrogenio','umidade'] else {
                    'ph':'pH','fosforo':'Fósforo','potassio':'Potássio','nitrogenio':'Nitrogênio','umidade':'Umidade'
                }[tipo]
                with cols[i]:
                    st.markdown(f"#### {titulo}")
                    fig, ax = plt.subplots()
                    ax.plot(df_t['dt_leitura'], df_t['vl_valor'], marker='o', linewidth=1)
                    ax.set_xticks(df_t['dt_leitura'][::max(1, len(df_t)//4)])
                    ax.tick_params(axis='x', rotation=45)
                    ax.set_ylabel('Valor')
                    ax.grid(True)
                    st.pyplot(fig)
        else:
            st.warning("Nenhuma leitura registrada.")

        st.markdown("---")

        # 🧪 Aplicações (Adubação & Fungicida)
        st.markdown("## 🧪 Aplicações")
        adubacoes = [r for r in listar_adubacoes(cursor) if r['cd_area'] == cd_area]
        fungicidas = [r for r in listar_fungicidas(cursor) if r['cd_area'] == cd_area]

        if adubacoes:
            st.markdown("### 🌾 Adubação")
            df_ad = pd.DataFrame([dict(r) for r in adubacoes])
            st.dataframe(
                df_ad[['dt_aplicacao','vl_quantidade','vl_fosforo','vl_potassio','vl_nitrogenio']],
                use_container_width=True
            )
        else:
            st.info("Nenhuma adubação registrada.")

        if fungicidas:
            st.markdown("### 🛡️ Fungicida")
            df_fun = pd.DataFrame([dict(r) for r in fungicidas])
            st.dataframe(
                df_fun[['dt_aplicacao','nm_produto','vl_quantidade']],
                use_container_width=True
            )
        else:
            st.info("Nenhuma aplicação de fungicida registrada.")

except Exception:
    st.error("Erro ao carregar dados do banco. Verifique a conexão.")
    import traceback
    st.text(traceback.format_exc())
