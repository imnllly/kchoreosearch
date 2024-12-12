import sqlite3
import sys
sys.path.insert(0, "app/")

from config import *
from db import *



sqlite_conn = sqlite3.connect("app/old_db/horeo.db")
sqlite_cur = sqlite_conn.cursor()

db_instance = db("postgres")
db_instance.drop_create("elements")

sqlite_cur.execute("SELECT id, group_name, members_num, gender, video_url, preview_url, video_name FROM elements")
elements = sqlite_cur.fetchall()

insert_query = "INSERT INTO elements (id, group_name, members_num, gender, video_url, preview_url, video_name) VALUES ({0});"

for element in elements:
    
    v = str([element[el] for el in range(len(element))])[1:-1]
    db_instance.query(insert_query.format(v))



sqlite_conn.close()