FROM python:3.10.0-alpine

WORKDIR /code

ENV FLASK_APP index.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . . 

CMD ["flask", "run"]