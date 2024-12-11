import math
from flask import render_template, request, Blueprint, session, redirect
from config import *
from db import db

main = Blueprint('main', __name__)
connect = db("postgres")

#---------------------------------------------------------------------------------------------------------------- Main Page ----------------------------------------------------------------------------------------------------------------

@main.route('/')
def index():

    if 'language' in session:

        language = session['language']


    else:

        language = "ru"

    
    search_query = request.args.get('search', "")
        
    videos = connect.select("SELECT * FROM groups WHERE group_name LIKE '%"+search_query+"%';")

    filtered_videos = []
    page = int(request.args.get('page', 0))
    filter_values = dict(request.args)

    print(request.args)


    if 'page' in filter_values:

        del filter_values['page']


    for video in videos:

        print(video)
        #if (len(filter_values) <= 1 or filter_values ):
        if len(filter_values) <= 1 or set([video[2], video[3]]).intersection(set(filter_values)):

            filtered_videos.append(video[4])


    pages = math.ceil(len(filtered_videos) / 12)

    filtered_videos = filtered_videos[12 * page: 12 * (page + 1)]

    if language == "ru":

        return render_template('index.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page)
    elif language == "en":
        return render_template('translate.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page)

#---------------------------------------------------------------------------------------------------------------- Login ----------------------------------------------------------------------------------------------------------------

@main.route('/login')
def login():
    return render_template('log.html')

#---------------------------------------------------------------------------------------------------------------- Login Check ----------------------------------------------------------------------------------------------------------------

@main.route('/login_check', methods=['POST', 'GET'])
def login_check():

    code = request.form['code']

    if(code==SECRET_CODE):

        return render_template('admin_page.html')
    

    return redirect('/')

#---------------------------------------------------------------------------------------------------------------- Add ----------------------------------------------------------------------------------------------------------------

@main.route('/add', methods=['POST', 'GET'])
def add():

    group_name = request.form['group_name']
    members_num = request.form['members_num']
    gender = request.form['gender']
    url = request.form['url']

    if(members_num.isdigit() and gender!=""):
        
        connect.query("INSERT INTO groups (group_name, members_num, gender, url) VALUES ('{0}', {1}, '{2}', '{3}');".format(group_name, members_num, gender, url))
    
    
    return redirect('/')

#---------------------------------------------------------------------------------------------------------------- Translate ----------------------------------------------------------------------------------------------------------------

@main.route('/translate')
def translate_en():

    session["language"] = "en"
    return redirect("/")


@main.route('/rus')
def translate_rus():

    session["language"] = "ru"
    return redirect("/")