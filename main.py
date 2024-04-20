import math

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

filter_groups = [
    {
        "title": "gender",
        "translate_title": "группы",
        "filters": [
            {
                "name": "BOY GROUP",
                "translate": "МУЖСКАЯ ГРУППА",
                "code": 'male'
            },
            {
                "name": "GIRL GROUP",
                "translate": "ЖЕНСКАЯ ГРУППА",
                "code": 'female'
            },
            {
                "name": "SWITCH GROUP",
                "translate": "СОВМЕСТНАЯ ГРУППА",
                "code": 'switch'
            }
        ]
    },
    {
        "title": "number",
        "translate_title": "кол-во участников",
        "filters": [
            {
                "name": "1 MEMBER",
                "translate": "1 УЧАСТНИК",
                "code": 'members_1'
            },
            {
                "name": "2 MEMBERS",
                "translate": "2 УЧАСТНИКа",
                "code": 'members_2'
            },
            {
                "name": "3 MEMBERS",
                "translate": "3 УЧАСТНИКА",
                "code": 'members_3'
            },
            {
                "name": "4 MEMBERS",
                "translate": "4 УЧАСТНИКА",
                "code": 'members_4'
            },
            {
                "name": "5 MEMBERS",
                "translate": "5 УЧАСТНИКОВ",
                "code": 'members_5'
            },
            {
                "name": "6 MEMBERS",
                "translate": "6 УЧАСТНИКОВ",
                "code": 'members_6'
            },
            {
                "name": "7 MEMBERS",
                "translate": "7 УЧАСТНИКОВ",
                "code": 'members_7'
            },
        ]
    }
]

@app.route('/')
def index():
    search_query = request.args.get('q') or ""
    with sqlite3.connect("horeo.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM groups WHERE `group` like ?", ('%' + search_query + '%',))
        videos = cur.fetchall()

        filtered_videos = []

        for video in videos:
            if len(request.args) <= 1 or set(video[6].split(',')).intersection(set(request.args)):
                filtered_videos.append(video[4])

        page = int(request.args.get('page', 0))

        pages = math.ceil(len(filtered_videos) / 12)

        filtered_videos = filtered_videos[12 * page: 12 * (page + 1)]
        return render_template('tasks.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page)

@app.route('/translate')
def translate():
    search_query = request.args.get('q') or ""
    with sqlite3.connect("horeo.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM groups WHERE `group` like ?", ('%' + search_query + '%',))
        videos = cur.fetchall()

        filtered_videos = []

        for video in videos:
            if len(request.args) <= 1 or set(video[6].split(',')).intersection(set(request.args)):
                filtered_videos.append(video[4])

        return render_template('translate.html', videos=filtered_videos, filter_groups=filter_groups)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)