from flask import Flask
import psycopg2
aoo = Flask(__name__)
def db_connect():
    conn = psycopg2.connect(
        dbname = 'hospital',
        user = 'postgres',
        password = 'root',
        host = 'localhost',
        port = '5432'
    )

    return conn
# table creation
@app.route('/create_table')
def table_create():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Patient(
            ))