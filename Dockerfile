# Dockerfile 4 DNon API Server

FROM python:3.8.3

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "manage.py", "run" ]