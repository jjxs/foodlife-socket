#!/bin/sh

/etc/init.d/nginx start
cd /code/
chmod -R 777 .
# uwsgi --ini uwsgi.ini --http-websockets
echo "uvicorn web.asgi:application --port 8080 --workers 4  --log-level trace  --access-log --use-colors --ws websockets"
# daphne -b 0.0.0.0 -p 8080  web.asgi:application
# python3 ./manage.py runserver 127.0.0.1:8080
# uvicorn  web.asgi:application --port 8080 --workers 4  --access-log /var/log/uvicorn.access.log  --log-level trace 
uvicorn web.asgi:application --port 8080 --workers 4  --log-level trace  --access-log --use-colors --ws websockets