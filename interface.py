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
        cidade = request.form.get("cidade").title()
        dia_atual = buscar_previsao_atual(cidade)
        proximos_dias = analisa_dia(cidade)

    html_template = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Previsão do Tempo</title>
        <style>
            * {
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }
            body {
                font-family: Arial, sans-serif;
                background-color: #00bbff;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .search-bar {
                margin: 20px 0;
                width: auto;
            }
            .input-field {
                padding: 10px;
                font-size: 18px;
                border-radius: 16px;
                border: 1px solid #ccc;
                width: 300px;
                text-align: center;
            }
            .submit-button {
                padding: 10px 20px;
                background-color: #0556f7;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 16px;
                font-size: 16px;
                cursor: pointer;
                transition: all ease 0.3s;
            }
            .submit-button:hover {
                outline: 5px solid rgba(240,240,240,0.7);
                background-color: #033cad;
            }
            .container {
                max-width: 1024px;
                width: 100%;
                margin: 0 auto;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }
            .current-weather {
                font-size: 36px;
                font-weight: bold;
                color: white;
                text-align: center;
                margin-bottom: 20px;
            }
            .weather-icon {
                width: 100px;
                height: 100px;
            }
            .forecast {
                display: grid;
                grid-template-columns: repeat(5, 1fr);
                justify-content: space-between;
                margin: 20px 0;
                gap: 20px;
            }
            .card {
                background-color: rgba(255, 255, 255, 0.7);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                flex: 1;
                height: 210px;
                display: flex;  
                flex-direction: column;
                gap: 8px;
                align-items: center;
            }
            .forecast-icon {
                width: 50px;
                height: 50px;
            }
            p {
                margin-bottom: 3px;
            }
            h2 {
                color: white;
            }

            @media (width < 768px) {
                .container {
                    max-width: 80%;
                }

                .forecast {
                    grid-template-columns: 1fr;
                }

                form {
                    display: flex;
                    flex-direction: column;
                    align-item: center;
                    gap: 8px;
                }
            }
        </style>
    </head>
    <body>

        <div class="container">
            <div class="search-bar">
                <form method="POST" action="/">
                    <input class="input-field" type="text" name="cidade" placeholder="Digite o nome da cidade" required>
                    <button class="submit-button" type="submit">Ver Previsão</button>
                </form>
            </div>

            {% if cidade %}
            <h2>Mostrando previsão para <u>{{ cidade }}</u>.</h2>
            <div class="current-weather">
                <img class="weather-icon" src="http://openweathermap.org/img/wn/{{ dia_atual['icone'] }}@2x.png" alt="Ícone de clima">
                <p>{{ dia_atual['temp'] }}ºC</p>
                <p>Hoje</p>
                <p>{{ dia_atual['clima'] }}</p>
            </div>

            <div class="forecast">
                {% for dia in proximos_dias %}
                <div class="card">
                    <h3>{{ dia['data'] }}</h3>
                    <img class="forecast-icon" src="http://openweathermap.org/img/wn/{{ dia['icone'] }}@2x.png" alt="Ícone de clima">
                    <p>{{ dia['temp'] }}ºC</p>
                    <p>{{ dia['temp_min'] }}ºC  -  {{ dia['temp_max'] }}ºC</p>
                    <p>{{ dia['clima'] }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(
        html_template, cidade=cidade, dia_atual=dia_atual, proximos_dias=proximos_dias
    )


if __name__ == "__main__":
    app.run(debug=True)
