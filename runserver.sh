#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn giveaway.wsgi -b 0.0.0.0:$PORT --log-file -
