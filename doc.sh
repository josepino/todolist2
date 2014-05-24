#!/bin/bash 
clear
echo "*****************Generando documentacion*****************"
cd todo/
sudo epydoc models.py admin.py test-raiz.py tests.py views.py

