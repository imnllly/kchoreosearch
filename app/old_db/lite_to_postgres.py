import sqlite3
import sys
sys.path.insert(0, "app/")

from config import *
from db import db


sqlite = db("sqlite")

db_instance = db("postgres")
db_instance.drop_create("elements")

elements = sqlite.select("SELECT id, group_name, members_num, gender, video_url, preview_url, video_name FROM elements")

insert_query = "INSERT INTO elements (id, group_name, members_num, gender, video_url, preview_url, video_name) VALUES ({0});"

for element in elements:
    
    v = str([element[el] for el in range(len(element))])[1:-1]
    db_instance.query(insert_query.format(v))