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
        temp_atual = data["main"]["temp"]
        descricao = data["weather"][0]["description"]

        print(f"Cidade: {cidade}")
        print(f"Temperatura: {int(temp_atual)}º")
        print(f"Condições: {descricao.capitalize()}")
    else:
        print("Cidade não encontrada ou erro na conexão.")

if __name__ == '__main__':
    cidade = input("Digite o nome da cidade: ")
    obter_previsao(cidade)