# Debuggear la aplicacion
"""
Cuando la aplicacion esta en ejecucion y el servidor esta levantado, si realizamos un cambio en el codigo no veremos
que afecte al servidor que se esa ejecutando. Esto se debe a que la aplicacion no se ha ejecutado con el debug mode
encendido, lo cual, permitira depurar el codigo mientras se realizan los cambios. sin el modo debug tendriamos que 
detener la ejecucion de la aplicacion y volver a iniciarla para ver si los cambios que realizamos ocasionan algun error
o tod esta bien.

Por el contrario, activando el modo debug el servidor se levanta y esta en modo escucha es decir que cualquier cambio
que se realice en el codigo, se actualizada directamente en el servidor y cuando refresquemos la pagina de nuestra
aplicacion veremos si tenemos un error mediante varios enunciados que especifican donde esta el error, de lo contrario,
la pagina aplicara los cambios al refrescarse.

# Para ejecutar el modo debug ingresamos el siguiente comando:

flask --app (nombre de la app) --debug run

Ej: flask --app hello --debug run

"""