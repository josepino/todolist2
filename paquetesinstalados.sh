#! /bin/bash
###### Script para obtener todo lo que esta instalado en la maquina
###### Usamos el comando apt-show-versions para ver los paquetes instalados en la maquina y guardamos en un archivo
#		apt-show-versions analiza el fichero de estado de dpkg y las listas de
#       APT en busca de las versiones de los paquetes instalados y disponibles
#       así como de la distribución de estos, y muestra las opciones de
#       actualización con la distribución especifica seleccionada para el
#       paquete.
apt-show-versions > instalados.txt