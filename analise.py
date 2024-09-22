import datetime
from previsao import buscar_previsao


def analisa_dia(cidade):
    dias = buscar_previsao(cidade)
    resultado = []

    for dia in dias:
        temp_min = float("inf")
        temp_max = float("-inf")
        climas = []
        temp = []

        for momento in dia:
            temp_min = int(min(temp_min, momento["temp_min"]))
            temp_max = int(max(temp_max, momento["temp_max"]))

            temp.append(int(momento["temp"]))
            climas.append(momento["clima"])

        temp = int(sum(temp) / len(temp))
        if any("chuva" in clima for clima in climas) and "céu limpo" in climas:
            clima = "Possibilidade de chuva"
        elif any("chuva" in clima for clima in climas):
            clima = "Chuvoso"
        elif "céu limpo" in climas:
            clima = "Ensolarado"
        elif any("nuvens" in clima for clima in climas):
            clima = "Nublado"
        else:
            clima = "Clima misto"

        data = datetime.datetime.fromtimestamp(momento["data"]).strftime("%d/%m/%Y")

        resultado.append(
            f"{temp}ºC\n{data}\nMin: {temp_min}ºC - Max: {temp_max}ºC\n{clima}"
        )

    return resultado
