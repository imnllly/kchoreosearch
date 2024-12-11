import math
from flask import render_template, request, Blueprint
from config import *
from db import db

main = Blueprint('main', __name__)
connect = db("postgres")

@main.route('/')
def index():

    search_query = request.args.get('q', "")
        
    videos = connect.select("SELECT * FROM groups WHERE group_name LIKE '%"+search_query+"%';")

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
        
    connect = db("postgres")
    videos = connect.select("SELECT * FROM groups WHERE group_name LIKE '%"+search_query+"%';")

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