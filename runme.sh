python manage.py migrate
gunicorn api.wsgi:application -p 8000 & nginx -g "daemon off;"