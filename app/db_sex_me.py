import sqlite3
import psycopg2
from config import *
from db import *

sqlite_conn = sqlite3.connect("app/horeo.db")
sqlite_cur = sqlite_conn.cursor()

db_instance = db("postgres")

db_instance.create()

sqlite_cur.execute("SELECT 'group', 'member', gender, video, 'preview', tags FROM groups")
videos = sqlite_cur.fetchall()

insert_query = "INSERT INTO groups (group_name, member, gender, video, preview, tags) VALUES ({0}, {1}, {2}, {3}, {4}, {5});"

for video in videos:
    print(insert_query.format(video[0], video[1], video[2], video[3], video[4], video[5]))
    db_instance.query(insert_query.format(
        "'"+video[0].replace("group", "aespa")+"'",
        "'"+video[1]+"'", 
        "'"+video[2]+"'", 
        "'"+video[3]+"'", 
        "'"+video[4]+"'", 
        "'"+video[5]+"'"))

sqlite_conn.close()