from flask import Flask

app = Flask(__name__)

# Como se observa tenemos dos rutas con sus respectivas vista y cada una de ellas es unica
@app.route('/')
def index():
    return 'Hello world'

@app.route('/bye')
def hello():
    return 'Goodbye world'

# Ademas de devolver texto plano las vistas(o funciones) tambien pueden devolver un HTML
@app.route('/hi')
def hi():
    return '<h1>Hi! How are you?</h1>'


