import sqlite3
import sys
sys.path.insert(0, "app/")

from config import *
from db import *



sqlite_conn = sqlite3.connect("app/old_db/horeo.db")
sqlite_cur = sqlite_conn.cursor()

db_instance = db("postgres")
db_instance.drop_create("groups")

sqlite_cur.execute("SELECT group_name, members, gender, video, prewew FROM groups")
videos = sqlite_cur.fetchall()

insert_query = "INSERT INTO groups ({0}) VALUES ({1});"

for video in videos:

    dict = {}

    if(video[0]): dict["group_name"] = video[0]
    if(video[1]): dict["members_num"] = video[1]
    if(video[2]): dict["gender"] = video[2]
    if(video[3]): dict["url"] = video[3]
    if(video[4]): dict["preview"] = video[4]
    

    g = str([i for i in dict])[1:-1].replace("'", "")
    v = str([dict.get(i) for i in dict])[1:-1]

    db_instance.query(insert_query.format(g, v))



sqlite_conn.close()