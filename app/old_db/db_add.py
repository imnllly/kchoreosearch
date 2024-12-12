import sqlite3
import sys
import requests

sys.path.insert(0, "app/")

from config import *
from db import *

sqlite_conn = sqlite3.connect("app/old_db/horeo.db")
sqlite_cur = sqlite_conn.cursor()

db_instance = db("postgres")
db_instance.create("elements")

i = input("Get ready for pizdec!\n")

while i!="0":

    dict = {}

    temp = input("Video url:\n")

    dict['id'] = temp[temp.find("video/")+6:-1]
    dict['group_name'] = input("Group name:\n").lower()
    dict['members_num'] = int(input("Members num:\n"))
    dict['gender'] = input("Gender:\n")
    dict['video_url'] = "https://rutube.ru/play/embed/"+dict.get('id')
    req = requests.get("https://rutube.ru/api/video/{}/thumbnail/?r...".format(dict.get('id')))
    dict['preview_url'] = req.text[req.text.find("url")+7:-2]
    dict['video_name'] = input("Video name:\n").lower()

    g = str([i for i in dict])[1:-1].replace("'", "")
    v = str([dict.get(i) for i in dict])[1:-1]

    sqlite_cur.execute("insert into elements ({0}) values ({1});".format(g, v))
    db_instance.query("insert into elements ({0}) values ({1});".format(g, v))
    sqlite_conn.commit()
    print("success!\n")