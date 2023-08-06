# Para crear una aplicacion con Flask, se debe importar desde el modulo flask la clase Flask 
from flask import Flask

# Instanciamos la clase Flask en la variable que va a representar a nuestra aplicacion
# Al pasar el atributo __name__ le estamos diciendo que este archivo es nuestra aplicacion o modulo principal y todos 
# los recursos los buscara aqui(Creo que aqui se refiere a la ruta donde se encuentra el modulo principal)
app = Flask(__name__)

# Creamos una ruta
# Si a la ruta le pasamos como parametro '/' estaremos indicando que la ruta que estamos creando es la ruta principal
# La cual debe estar asociada a una funcion que representa una vista, ya que cada ruta en flask debe estar asociado a
# a una funcion.
@app.route('/')
def helloWorld():
    return 'Hello World'

"""
Nota1:
@app. route es un decorador que convierte una función Python regular en una función vista de Flask, que convierte el 
valor de devolución de la función en una respuesta HTTP que se mostrará mediante un cliente HTTP, como un navegador web
"""

"""
NOta2:
El primer argumento es el nombre del módulo o paquete de la aplicación. __name__ es un atajo conveniente para esto 
que es apropiado para la mayoría de los casos. Esto es necesario para que Flask sepa dónde buscar recursos como 
plantillas y archivos estáticos.
"""