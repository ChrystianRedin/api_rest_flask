import os
from psycopg2 import connect

host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")
dbname = os.environ.get("POSTGRES_NAME")
user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")

def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,
                   user=user, password=password)
    return conn
