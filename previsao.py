import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def obter_previsao(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cidade = data["name"]
        temp_atual = int(data["main"]["temp"])
        descricao = data["weather"][0]["description"].capitalize()

        print(f"Cidade: {cidade}")
        print(f"Temperatura: {temp_atual}º")
        print(f"Condições: {descricao.capitalize()}")
        return f"Previsão do tempo para {cidade}:\n{temp_atual}º\n{descricao}"
    else:
        print("Cidade não encontrada ou erro na conexão.")
        return "Cidade não encontrada ou erro na conexão."
