from flask import Flask, render_template_string, request
from previsao import buscar_previsao_atual
from analise import analisa_dia

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def mostrar_previsao():
    cidade = None
    dia_atual = None
    proximos_dias = None

    if request.method == "POST":
        cidade = request.form.get("cidade")  # Obtém a cidade inserida pelo usuário
        dia_atual = buscar_previsao_atual(cidade)
        proximos_dias = analisa_dia(cidade)

    # Definindo o template HTML com barra de pesquisa estilizada e cards
    html_template = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Previsão do Tempo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                padding: 0;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            header {
                background-color: #0366d6;
                padding: 20px;
                width: 100%;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: white;
                margin: 0;
            }
            .search-bar {
                margin: 20px 0;
            }
            .input-field {
                padding: 10px;
                font-size: 18px;
                border-radius: 25px;
                border: 1px solid #ccc;
                width: 300px;
                text-align: center;
            }
            .submit-button {
                padding: 10px 20px;
                background-color: #0366d6;
                color: white;
                border: none;
                border-radius: 25px;
                font-size: 16px;
                cursor: pointer;
            }
            .submit-button:hover {
                background-color: #024b9c;
            }
            .container {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 20px;
            }
            .current-weather {
                font-size: 48px;
                font-weight: bold;
                color: #333;
                text-align: center;
                margin-bottom: 20px;
            }
            .weather-icon {
                width: 100px;
                height: 100px;
            }
            .forecast {
                display: flex;
                justify-content: space-between;
                width: 80%;
                margin-top: 20px;
                gap: 20px;
            }
            .card {
                background-color: white;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                flex: 1;
            }
            .card h3 {
                margin-top: 0;
            }
            .forecast-icon {
                width: 50px;
                height: 50px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Previsão do Tempo</h1>
        </header>

        <div class="search-bar">
            <form method="POST" action="/">
                <input class="input-field" type="text" name="cidade" placeholder="Digite o nome da cidade" required>
                <button class="submit-button" type="submit">Ver Previsão</button>
            </form>
        </div>

        {% if cidade %}
        <div class="container">
            <div class="current-weather">
                <img class="weather-icon" src="http://openweathermap.org/img/wn/{{ dia_atual['icone'] }}@2x.png" alt="Ícone de clima">
                <p>{{ dia_atual['temp'] }}ºC</p>
                <p>{{ dia_atual['clima'] }}</p>
            </div>

            <div class="forecast">
                {% for dia in proximos_dias %}
                <div class="card">
                    <h3>{{ dia['data'] }}</h3>
                    <img class="forecast-icon" src="http://openweathermap.org/img/wn/{{ dia['icone'] }}@2x.png" alt="Ícone de clima">
                    <p>{{ dia['temp'] }}ºC</p>
                    <p>Min: {{ dia['temp_min'] }}ºC - Max: {{ dia['temp_max'] }}ºC</p>
                    <p>{{ dia['clima'] }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html_template, cidade=cidade, dia_atual=dia_atual, proximos_dias=proximos_dias)

if __name__ == "__main__":
    app.run(debug=True)
