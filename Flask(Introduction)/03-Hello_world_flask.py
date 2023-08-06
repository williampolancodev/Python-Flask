# Creando la aplicacion Hello world
"""
Como ya creamos y configuramos el entorno virtual vamos a crear nuesta primera app con flask y sera el programa 
clasico que ejecutamos cuando aprendemos un nuevo lenguaje 'Hellos World' para ello creamos un archivo hello.py
el cual, tiene que tener como interprete el archivo de python.exe que se encuentra dentro del entorno virtual que
creamos para saber que estamos trabajando dentro del entorno virtual. Para ello, podemos hacer dos cosa 
configurarlos desde VSC o abrir VSC desde la consola de windows.

- Para congigurarlo desde VSC hacemos clic donde se refleja el interprete que estamos utilizando que la parte inferior
derecha, nos saldra una ventana para seleccionar el interprete o añadir una nueva ruta para el interprete. En nuestro caso
añadimos la nueva ruta y buscamos dentro de nuestro entorno en nuestra carpeta Scripts el archivo python.exe y asi se estara
utilizando el interprete del entorno.

- Para hacerlo por consola solo tendremos que ir a la ruta donde se encuentra nuestra app con su entorno virtual,
y despues activar el entorno virtual. Y finalmente ejecutar el comando 'code .' para abrir en VSC la ruta actual
donde nos encontramos ubicados en la terminal
"""

# Ejecutando la aplicacion hello world
""""
Para ejecutar nuestra aplicacion debemos colocar en nuestra consola el comando 'flask --app (nombre de la app) run'
Esto ejecuara un servidor de desarrollo y nos dara una ip con el puerto en que se ejecuta el servidor y al darle click
abrira el navegador en esa direccion y nos mostrara lo que haga nuestra app.
Ej: flask --app hello run
"""