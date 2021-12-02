import os
import bandeiras
from flask import Flask, render_template, request

app = Flask(__name__)


def nome_pais(pais):
    return {
        'franca': 'França',
        'japao': 'Japão',
        'dinamarca': 'Dinamarca',
        'porto_rico': 'Porto Rico',
        'italia': 'Itália',
        'islandia': 'Islândia',
        'irlanda': 'Irlanda',
        'alemanha': 'Alemanha',
        'reino_unido': 'Reino Unido',
        'tanzania': 'Tanzânia',
        'nigeria': 'Nigéria'

    }.get(pais)


def imagens_pais(pais):
    return {16: f'static/images/{pais}-16.png',
            32: f'static/images/{pais}-32.png',
            64: f'static/images/{pais}-64.png',
            128: f'static/images/{pais}-128.png',
            256: f'static/images/{pais}-256.png',
            512: f'static/images/{pais}-512.png',
            1024: f'static/images/{pais}-1024.png'}


@app.route('/')
def index():
    pais_atual = 'franca'
    return render_template('index.html', pais=nome_pais(pais_atual), imagens=imagens_pais(pais_atual))


@app.route('/', methods=['POST'])
def selecionar():
    pais_atual = request.form['pais']
    return render_template('index.html', pais=nome_pais(pais_atual), imagens=imagens_pais(pais_atual))


bandeiras.gerar_imagens()
port = int(os.environ.get("PORT", 8080))
app.run(host='0.0.0.0', port=port)
