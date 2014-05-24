#!/bin/bash 

clear
echo "********************Borrando y Creando la Base de Datos********************"
sudo -u postgres psql -f borrar.sql
echo "********************Poblando la Base de Datos********************"
sudo -u postgres psql -f poblacion.sql dbpm

