import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
CIDADE = os.getenv("CIDADE")


def obter_dados_climaticos():
    """
    Consulta a API OpenWeather e retorna temperatura, umidade, precipitação e condição atual da cidade.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperatura = data["main"]["temp"]
        umidade = data["main"]["humidity"]
        precipitacao = data.get("rain", {}).get("1h", 0.0)
        condicao = data["weather"][0]["description"]

        return temperatura, umidade, precipitacao, condicao

    except Exception as e:
        print("❌ Erro ao obter dados do clima:")
        import traceback
        traceback.print_exc()
        return None, None, None, None
