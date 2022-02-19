FROM python:3.10
WORKDIR /app
ADD . /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD [ "uwsgi", "--ini", "wsgi-config.ini" ]