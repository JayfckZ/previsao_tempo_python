# Previsão do Tempo Dinâmica 

 Este projeto é uma aplicação simples que permite ao usuário consultar a previsão do tempo em tempo real para qualquer cidade, utilizando a API da OpenWeather. O projeto foi desenvolvido com o framework Flask e possui uma interface amigável e estilosa, com suporte para múltiplas previsões climáticas.

## Funcionalidades

- **Busca de Previsão por Cidade**: Pesquise o clima em qualquer cidade diretamente pela barra de pesquisa.
- **Temperatura Atual**: Veja a temperatura atual da cidade em destaque.
- **Previsão para os Próximos Dias**: Consulte as previsões para os próximos dias em cartões estilizados.
- **Ícones Climáticos**: Apresentação de ícones que representam as condições climáticas.
- **Design Responsivo**: Interface adaptada para diversos tamanhos de tela, incluindo desktops e dispositivos móveis.


## Tecnologias Utilizadas

- **Linguagem**: Python 3.12.6
- **Framework**: Flask 3.0.3
- **Bibliotecas Adicionais**:
  - `python-dotenv 1.0.1`: Para carregar variáveis de ambiente.
  - `requests 2.32.3`: Para fazer requisições HTTP à API da OpenWeather.
## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/JayfckZ/previsao_tempo_python
   cd weather-now
   ```

2. **Crie um ambiente virtual**
    ```bash
    python -m venv venv
    source venv/bin/activate
    # No Windows use `venv\\Scripts\\activate`
    ```

3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configuração da API Key**
    Crie um arquivo `.env` na raiz do projeto e adicione a chave da API da OpenWeather:
    ```makefile
    API_KEY=sua_openweather_api_key
    ```

5. **Execute**
    ```bash
    python interface.py
    ```
## Funções

Função: `obter_coords(cidade)`:
Busca as coordenadas de latitude e longitude de uma cidade a partir da API da OpenWeather.

Função: `buscar_previsao_atual(cidade)`:
Retorna a previsão atual de temperatura e condição climática para uma cidade, incluindo o ícone correspondente.

Função: `buscar_previsao(cidade)`:
Retorna a previsão do tempo para os próximos dias (com intervalos de 3 horas), apresentando dados de temperatura mínima e máxima, além de condições climáticas.

Função: `analisa_dia(cidade)`:
Faz a análise das condições climáticas de uma cidade para determinar a média de temperatura e prever as condições para cada dia.

