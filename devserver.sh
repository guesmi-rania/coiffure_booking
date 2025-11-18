#!/bin/sh
source .venv/bin/activate
python manage.py runserver $PORT  # plus besoin de mysite/manage.py
