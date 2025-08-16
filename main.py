from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

perfil = {
    'nombre': 'Xenon',
    'descripcion': 'Programador dedicado al desarrollo de paginas webs, bots entre otras cosas.',
    'email': 'tu@email.com',
    'github': 'https://github.com/angelosanchezcuripuma37-ops',
    
    'sobre_mi': 'Soy un programador dedicado actualmente al desarrollo de páginas webs y bots para la plataforma de Discord entre otros servicios más.',

    'resenas': [
        ''
    ],

    'proyectos': [
        {
            'titulo': 'Zona Norte RP|Bot',
            'descripcion': 'Bot hecho para la comunidad de Zona Norte RP. Cuenta con funciones de moderación, roleplay y un sistema de tickets personalizado.'
        },
        {
            'titulo': 'Todo sobre discol|Bot',
            'descripcion': 'Este bot fue utilizado un tiempo en la comunidad de "Todo sobre discord" el mismo contaba con comandos de moderación y otras opciónes más.'
        },
        {
            'titulo': 'Imperial Motors|Bot',
            'descripcion': 'Bot hecho para una empresa de roleplay dentro de la comunidad de TIERRA MEXICO RP.'
        },
        {
            'titulo': '',
            'descripcion': '.'
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', perfil=perfil, now=datetime.now())

if __name__ == '__main__':
    app.run(debug=True)
