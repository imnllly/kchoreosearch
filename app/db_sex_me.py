import sqlite3
import psycopg2
from config import *


sqlite_conn = sqlite3.connect("horeo.db")
sqlite_cur = sqlite_conn.cursor()


pg_conn = psycopg2.connect(
    dbname='your_postgres_db_name',
    user=DATABASE_LOGIN,
    password=DATABASE_PASSWORD,
    host="localhost",
    port="5432"
)
pg_cur = pg_conn.cursor()


sqlite_cur.execute("SELECT group, member, gender, video, preview, tags FROM groups")  
videos = sqlite_cur.fetchall()


insert_query = """
    INSERT INTO groups (group_name, member, gender, video, preview, tags)
    VALUES (%s, %s, %s, %s, %s, %s)
"""

for video in videos:
    pg_cur.execute(insert_query, video)


pg_conn.commit()
sqlite_conn.close()
pg_conn.close()
