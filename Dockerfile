FROM python:alpine
RUN apk update 


ENV APP_HOST='0.0.0.0' \
APP_PORT='8080' \
APP_DEBUG_MODE=True



WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python","-m", "server.app"]