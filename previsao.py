import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def obter_coords(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]

        return lat, lon
    else:
        print("Cidade não encontrada ou erro na conexão.")
        return "Cidade não encontrada ou erro na conexão."

def buscar_previsao_atual(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = int(data["main"]["temp"])
        clima = data["weather"][0]["description"].capitalize()
        icone = data["weather"][0]["icon"]
        return {"temp": temp, "clima": clima, "icone": icone}
    else:
        return "Cidade não encontrada ou erro na conexão."


def buscar_previsao(cidade):
    lat, lon = obter_coords(cidade)

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        previsao = data["list"]

        resultado = []
        dia_atual = []
        i = 0
        for dia in previsao:
            temp = dia["main"]["temp"]
            t_min = dia["main"]["temp_min"]
            t_max = dia["main"]["temp_max"]
            date = dia["dt"]
            descricao = dia["weather"][0]["description"]
            icone = dia["weather"][0]["icon"]
            dia_atual.append({"data": date, "temp": temp, "temp_min": t_min, "temp_max": t_max, "clima": descricao, "icone": icone})
            i += 1
            if i == 8:
                i = 0
                resultado.append(dia_atual)
                dia_atual = []
        return resultado
    else:
        return None
