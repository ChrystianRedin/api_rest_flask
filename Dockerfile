FROM python:3.9.0-alpine

WORKDIR /code

ENV FLASK_APP index.py

ENV FLASK_RUN_HOST 0.0.0.0

# RUN apk add --no-cache gcc musl-dev linux-headers

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . . 

CMD ["flask", "run"]