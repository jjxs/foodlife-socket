FROM python:3.7.3
RUN mkdir /code
WORKDIR /code
COPY code/requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN pip3 install uvicorn[standard]
RUN apt update
RUN apt-get install -y nginx
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/default.conf /etc/nginx/conf.d/default.conf
COPY code/ /code/
RUN apt-get install -y vim strace
# RUN pip3 install uwsgi
# COPY conf/uwsgi.ini /code/

RUN useradd nginx
ADD ./conf/start.sh /tmp/start.sh
CMD /bin/sh /tmp/start.sh
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8002"]