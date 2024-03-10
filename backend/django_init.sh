#!/bin/bash
# /codeがDockerfileのWORKDIR
cd /code/django_app
# python3 -m pip install -r requirements.txt  # pythonパッケージ
python manage.py migrate
python manage.py createsuperuser --noinput
#python3 manage.py runserver 0.0.0.0:8000
bash
