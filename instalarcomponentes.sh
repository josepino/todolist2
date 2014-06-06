#!/bin/bash

### Scripts de instalacion de los componentes

echo "/////////////////////////////"
echo "     PROJECT MANAGEMENT"
echo " Instalacion de componentes"
echo "         Autores:"
echo "        Jose Pino"
echo "     Jose Santacruz"
echo "       Victor Vera"
echo "/////////////////////////////"

echo "Ultima actualizacion 06 Junio 2014"


########################Variable Directorio del proyecto
directorioinstalacion="/home/jose/PycharmProjects/todolist2"

#########################Variable Superuser a crear en la BD
user='postgres'

#########################Variable Pass del super user a crear en la BD
pass='postgres'

#########################Variable Directorio actual del instalador
directorioinstalador=`pwd`

##########################Variable Codigo fuente del proyecto
fuente="https://github.com/josepino/todolist2/archive/master.zip"



##########################Paquetes instalados actualmente
#Obtenemos los paquetes instalados y guardamos en un archivo temporal
apt-show-versions > pqtesinstalados.txt

if [ ! -d "$directorioinstalacion" ];
then
	echo "El directorio no existe, se creara el directorio necesario"
	mkdir -p "$directorioinstalacion"
fi



#########################Verificamos si tenemos en el archivo 
#########################los componentes necesarios, si esta es por que ya esta instalado en la maquina,
#########################caso contrario instalamos:

#########################Python 2.7
instalado=`grep python2.7 instalados.txt`
if [ -n "$instalado" ];
then
	echo "Python2.7 ya esta instalado"
else
	echo "Instalacion de Python2.7"
	sudo apt-get install python
fi


##########################Django
if [ -d /usr/local/lib/python2.7/dist-packages/django ];
then
	echo "Django ya esta instalado"
else
	echo "Instalacion de Django"
	sudo apt-get install django
fi


##########################Apache
instalado=`grep apache2 instalados.txt`
if [ -n "$instalado" ];
then
	echo "Apache2 ya esta instalado"
else
	echo "Instalacion de Apache2"
	apt-get  install apache2
fi


##########################Postgresql
instalado=`grep postgresql instalados.txt`
if [ -n "$instalado" ];
then
	echo "Postgresql ya esta instalado"
else
	echo "Instalacion de Postgresql"
	apt-get install postgresql



##########################Psycopg2
instalado=`grep python-psycopg2 instalados.txt`
if [ -n "$instalado" ];
then
	echo "La libreria python-psycopg2 ya esta instalado"
else
	echo "Instalacion de python-psycopg2"
	apt-get install python-psycopg2
fi




#############Instalacion Proyecto PM
#############Vemos si ya esta instalado, sino obtenemos del repositorio
if [ -d "$directorioinstalacion/todolist2" ];
then
	echo "El proyecto ya se encuentra instalado"
else
if [ ! -d proyecto ];
then
	#Usamos wget para bajar: GNU Wget is a free utility for non-interactive download of files from the Web.
	wget "$fuente" -P proyecto
fi

#Una vez bajado el proyecto nos vamos hasta ahi y procedemos a descomprimir
cd proyecto
unzip master.zip


##############Verificamos los archivos de configuracion
##############Archivo de configuracion todolist.wsgi
#Vemos la ruta donde se encuentra
ruta_todolist_wsgi="$directorioinstalacion/todolist"
#Vemos si esta instalado
instalado=`ls "$ruta_todolist_wsgi" | grep todolist.wsgi`

#Si ya existe el archivo borramos para crear y cargar de nuevo con las variables del sistema local
if [ "$wsgi_conf" ];
then
	echo "Ya existe el archivo, se sobreescribira con las variables locales de la maquina"
	rm "$ruta_todolist_wsgi/todolist.wsgi"
fi

#Creamos y cargamos los datos en el archivo de configuracion
if [ -n "$wsgi_conf" ];
then
	echo "Creando y agregando datos al archivo todolist.wsgi"
	echo "import os" > todolist.wsgi
	echo "import sys" >> todolist.wsgi
	echo "sys.path = ['"$ruta_todolist_wsgi"'] + sys.path" >> todolist.wsgi
	echo "os.environ['DJANGO_SETTINGS_MODULE'] = 'todolist.settings'" >> todolist.wsgi
	echo "import django.core.handlers.wsgi" >> todolist.wsgi
	echo "application = django.core.handlers.wsgi.WSGIHandler()" >> todolist.wsgi
fi







#############Base de Datos
#        'NAME': 'dbpm',
#        'USER': 'postgres',
#        'pass': 'postgres',


############Creamos un user
#El comando es createuser con los parametros (quitados de la documentacion man createuser):
# -d The new user will be allowed to create databases.
# -l The new user will be allowed to log in (that is, the user name can be used as the initial session user identifier). This is the default.
# -P If given, createuser will issue a prompt for the pass of the new user. This is not necessary if you do not plan on using pass authentication.
# -r The new user will be allowed to create new roles (that is, this user will have CREATEROLE privilege).
# -S The new user will not be a superuser.
# -U User name to connect as (not the user name to create).

##############Ejecucion del comando
createuser -d -l -P -r -S postgres -U postgres

if [ $? -ne 0 ]; then
	echo -e "\nPosible error ocurrido, revisar archivos y documentacion."
    exit
fi

echo -e "\n\nEl user se ha creado."

##############Creacion de la BD con el user postgres, poblacion.sql es un archivo que esta en el mismo directorio
########ACTUALIZA!!!!!!! psql -U postgres postgres -f poblacion.sql

if [ $? -ne 0 ]; then
	echo "Ha ocurrido un error, revisar archivos y documentacion."
fi

python syncdb.py


##################Lanzar el navegador
firefox -new-tab 127.0.0.1:8000/admin
#google-chrome -new-tab 127.0.0.1:8000/admin
#chromium-browser -new-tab 127.0.0.1:8000/admin






exit
