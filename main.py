import bandeiras
from flask import Flask, render_template, request

app = Flask(__name__)


def nome_pais(pais):
    return {
        'franca': 'França',
        'japao': 'Japão'
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
app.run(host='localhost', port=8080)
