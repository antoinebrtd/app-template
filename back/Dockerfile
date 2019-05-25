FROM python:3.6

RUN mkdir -p /app/config
WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD config/config.prod.json /app/config/config.json
ADD config/google.json /app/config/google.json
ENV CONFIG_FILE /app/config/config.json

ADD run.py /app/
ADD worker.py /app/

ADD template /app/template

CMD ["gunicorn","-w","1","--bind","0.0.0.0:8000","run:app"]
