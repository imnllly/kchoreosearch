import math
from flask import Flask, render_template, request, Blueprint
import sqlite3
from config import *


main = Blueprint('main', __name__)


@main.route('/')
def index():

    search_query = request.args.get('q', "")
    
    with sqlite3.connect("app/horeo.db") as conn:

        cur = conn.cursor()
        print(search_query)
        cur.execute("SELECT * FROM groups WHERE `group` like ?", ('%' + search_query + '%',))
        videos = cur.fetchall()

        filtered_videos = []
        page = int(request.args.get('page', 0))

        filter_values = dict(request.args)

        if 'page' in filter_values:

            del filter_values['page']


        for video in videos:

            if len(filter_values) <= 1 or set(video[6].split(',')).intersection(set(filter_values)):
                filtered_videos.append(video[4])


        pages = math.ceil(len(filtered_videos) / 12)

        filtered_videos = filtered_videos[12 * page: 12 * (page + 1)]

        return render_template('tasks.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page)



@main.route('/translate')
def translate():

    search_query = request.args.get('q', "")

    with sqlite3.connect("app/horeo.db") as conn:

        cur = conn.cursor()
        print(search_query)
        cur.execute("SELECT * FROM groups WHERE `group` like ?", ('%' + search_query + '%',))
        videos = cur.fetchall()

        filtered_videos = []
        page = int(request.args.get('page', 0))

        filter_values = dict(request.args)

        if 'page' in filter_values:

            del filter_values['page']


        for video in videos:

            if len(filter_values) <= 1 or set(video[6].split(',')).intersection(set(filter_values)):

                filtered_videos.append(video[4])


        pages = math.ceil(len(filtered_videos) / 12)

        filtered_videos = filtered_videos[12 * page: 12 * (page + 1)]
        return render_template('translate.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page)

#b.query("INSERT INTO songs (name) VALUES ('{}');".format("ZZZ"))