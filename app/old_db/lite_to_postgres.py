import sqlite3
import sys
sys.path.insert(0, "app/")

from config import *
from db import db


sqlite = db("sqlite")
psotgres = db("postgres")

psotgres.drop_create("elements")

elements = sqlite.select("SELECT id, group_name, members_num, gender, video_url, preview_url, video_name FROM elements")

insert_query = "INSERT INTO elements (id, group_name, members_num, gender, video_url, preview_url, video_name) VALUES ({0});"

for element in elements:
    
    v = str([element[el] for el in range(len(element))])[1:-1]
    psotgres.query(insert_query.format(v))