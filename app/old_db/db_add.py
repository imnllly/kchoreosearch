import sqlite3
import sys
import requests

sys.path.insert(0, "app/")

from config import *
from db import db


sqlite = db("sqlite")
postgres = db("postgres")

while True:

    dict = {}

    url = input("Video url:\n")

    dict['id'] = url[url.find("video/")+6:-1]
    dict['group_name'] = input("Group name:\n").lower()

    el = postgres.select("select * from elements where group_name = '{}';".format(dict.get('group_name')))

    if(el):
    
        el=el[0]  
        dict['members_num'] = int(el[2])
        dict['gender'] = el[3]


    else:

        dict['members_num'] = int(input("Members num:\n"))
        dict['gender'] = input("Gender:\n")


    dict['embed_url'] = "https://rutube.ru/play/embed/"+dict.get('id')
    req = requests.get("https://rutube.ru/api/video/{}/thumbnail/?r...".format(dict.get('id')))
    dict['preview_url'] = req.text[req.text.find("url")+7:-2]
    dict['video_name'] = input("Video name:\n").lower()
    dict['video_url'] = url

    g = str([i for i in dict])[1:-1].replace("'", "")
    v = str([dict.get(i) for i in dict])[1:-1]

    sqlite.query("insert into elements ({0}) values ({1});".format(g, v))
    postgres.query("insert into elements ({0}) values ({1});".format(g, v))

    print("\nSuccess!\n")