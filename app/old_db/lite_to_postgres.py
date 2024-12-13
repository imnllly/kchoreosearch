import sqlite3
import sys
sys.path.insert(0, "app/")

from config import *
from db import db


sqlite = db("sqlite")
psotgres = db("postgres")

psotgres.drop_create("elements")

elements = sqlite.select("SELECT * FROM elements")

insert_query = "INSERT INTO elements (id, group_name, members_num, gender, embed_url, preview_url, video_name, video_url) VALUES ({0});"

for element in elements:
    
    v = str([element[el] for el in range(len(element))])[1:-1]
    psotgres.query(insert_query.format(v))