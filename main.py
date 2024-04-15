from flask import Flask, render_template, request
import sqlite3

# import sqlalchemy

app = Flask(__name__)

#здесь список с группами
filter_groups = [
    {
        "title": "gender", #КОД ДЛЯ ТИТЛОВ
        "translate_title": "группы", #КОД ДЛЯ ПЕРЕВОДА ТИТЛОВ
        "filters": [
            {
                "name": "BOY GROUP", #КОД ДЛЯ НАЗВАНИЯ ФИЛЬТРОВ
                "code": 'male' #КОД ДЛЯ ПЕРЕВОДА ФИЛЬТРОВ
            },
            {
                "name": "GIRL GROUP",
                "code": 'female'
            },
            {
                "name": "SWITCH GROUP",
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

        return render_template('tasks.html', videos=filtered_videos, filter_groups=filter_groups)


if __name__ == '__main__':
    app.run(debug=True)
