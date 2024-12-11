import sqlite3
import psycopg2
from config import *
from db import * # Импортируйте класс db из файла db.py

# Подключение к SQLite
sqlite_conn = sqlite3.connect("horeo.db")
sqlite_cur = sqlite_conn.cursor()

# Подключение к PostgreSQL и создание объекта db
pg_conn = psycopg2.connect(
    dbname='postgres',
    user=DATABASE_LOGIN,
    password=DATABASE_PASSWORD,
    host="localhost",
    port="5432"
)
db_instance = db(pg_conn)  # Создайте экземпляр класса db, передав соединение

# Создание таблицы в PostgreSQL
db_instance.create()

# Получение данных из таблицы SQLite
sqlite_cur.execute("SELECT group, member, gender, video, preview, tags FROM groups")
videos = sqlite_cur.fetchall()

# SQL-запрос для вставки данных в PostgreSQL
insert_query = """
    INSERT INTO groups (group_name, member, gender, video, preview, tags)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

# Вставка данных в таблицу PostgreSQL
for video in videos:
    pg_conn.cursor().execute(insert_query, video)

# Коммит изменений и закрытие соединений
pg_conn.commit()
sqlite_conn.close()
pg_conn.close()
