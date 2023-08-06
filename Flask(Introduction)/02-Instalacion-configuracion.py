# Instalacion
""""
Bastara con ir a la pagina oficial de flask y seguir los pasos para instalarlo, mayormente se sugiere crear un entorno
virtual de python e instalar flask en el entorno virutal de nuestro proyecto. De esa manera podemos tener la version
de flask necesaria con nuestro proyecto y  no tener diferentes versiones instaladas que puedan afectarse entre si.

- Crear entorno virtual
    Hay varias formas de crear el entorno virtual en este caso utilizaremos venv que es un paquete que viene con python
    3. Tambien estan las opciones como la biblioteca virtualenv que ofrece mas funcionalidades de venv o pipenv que
    tambien ofrece mas funcionalidades y algunas comodidas, el cual, es el comunmente utilizado por sus ventajas.

    Para crear el entorno virtual con venv escribimos el siguiente comando(python -m venv +(nombre del entorno)) 
    desde la consola y en la ruta que queremos crear el entorno.
    Ej: python -m venv myproject-env

- Activarlo
    Para activarlo solo hay que ingresar la ruta necesaria para ejecutar el "activate", mayormente seria:
    (nombre del entorno)\Scripts\activate.
    Ej:myproject-env\Scripts\activate
    Nota: la rutas se ingresan utilizando barra diagonal hacia la derecha (\)

    Ahora antes de la ruta donde estamos deveria aparecer el nombre del entorno entre parentesis, indicando que esta
    activo.
    EJ: (myproject-env) C:\Workspace\Python-Flask\myproject>

- Instalar flask
    Antes de instalar flask podemos ingresar el comando 'pip list' para ver las herramientas que estan instaladas en el
    entorno. Y veremos que solo tendremos dos 'pip' y 'setuptools' cada una con su version especificada. Y despues de eso
    recibiremos un mensaje de advertencia para que actualicemos la version de pip si no poseemos la ultima. Y siguiendo las
    instrucciones desde la misma consola utilizando el comando que nos sugiere, actualizaremos 'pip'

    NOta: si queremos intalar una version en especifico de un paquete debemos indicarlo de la siguiente manera 
    'pip install (nombre del paquete)==(version del paquete)'
        Ej: pip install setuptools==68.0.0

    Despues simplemente ejecutamos: pip install flask
    Y se comenzara a instalar flask y todas sus dependencias, una vez termiando ejecutamos 'pip list' y veremos:
    Package      Version
------------ -------
blinker      1.6.2
click        8.1.6
colorama     0.4.6
Flask        2.3.2
itsdangerous 2.1.2
Jinja2       3.1.2
MarkupSafe   2.1.3
pip          23.2.1
setuptools   58.1.0
Werkzeug     2.3.6

Nota: Investigar que hacen las dependencias de flask

Ahora para desactivar el entorno utilizamos el comando 'deactivate'
Recor


"""