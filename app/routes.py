import math
from flask import render_template, request, Blueprint, session, redirect
from config import *
from db import db

main = Blueprint('main', __name__)
connect = db("postgres")

#---------------------------------------------------------------------------------------------------------------- Main Page ----------------------------------------------------------------------------------------------------------------

@main.route('/', methods=['POST', 'GET'])
def index():

    if 'language' in session:

        language = session['language']


    else:

        language = "ru"

    search = request.args.get('search', "")
    gender = request.args.get('gender', "")
    number = request.args.get('number', "")

    select_query = "SELECT * FROM elements WHERE group_name LIKE '%"+search+"%'{0}{1};"

    if(gender!=""):gender=" and gender = '"+gender+"'"
    if(number!=""):number=" and members_num = '"+number+"'"

    videos = connect.select(select_query.format(gender, number))

    filtered_videos = []
    page = int(request.args.get('page', 0))
    filter_values = dict(request.args)

    if 'page' in filter_values:

        del filter_values['page']


    for video in videos:

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

        return render_template('admin_get.html')
    

    return redirect('/')

#---------------------------------------------------------------------------------------------------------------- Add ----------------------------------------------------------------------------------------------------------------

#@main.route('/add', methods=['POST', 'GET'])
#def add():
#
#    group_name = request.form['group_name']
#    members_num = request.form['members_num']
#    gender = request.form['gender']
#    url = request.form['url']
#
#    if(members_num.isdigit() and gender!=""):
#        
#        connect.query("INSERT INTO elements (group_name, members_num, gender, url) VALUES ('{0}', {1}, '{2}', '{3}');".format(group_name, members_num, gender, url))
#    
#    
#    return redirect('/')

#---------------------------------------------------------------------------------------------------------------- Add ----------------------------------------------------------------------------------------------------------------

@main.route('/get', methods=['POST', 'GET'])
def get():

    id = request.form['id']

    l = ""

    if(id.isdigit()):
        
        l = str(connect.select("SELECT * FROM elements WHERE id = {};".format(id))).replace("'", "")[2:-2].split(", ")
        
    
    return render_template('admin_get.html', list=l)

#---------------------------------------------------------------------------------------------------------------- Remove ----------------------------------------------------------------------------------------------------------------

@main.route('/remove', methods=['POST', 'GET'])
def remove():

    field_type = request.form['type']
    value = request.form['value']

    if(field_type!="" and value):

        connect.query("DELETE FROM elements where {0} = '{1}';".format(field_type, value))

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