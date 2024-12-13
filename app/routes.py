import math
from flask import render_template, request, Blueprint, session, redirect
from config import *
from db import db
import requests

main = Blueprint('main', __name__)

connect = db()

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
        
        filtered_videos.append([video[4], video[5]])


    pages = math.ceil(len(filtered_videos) / 12)

    filtered_videos = filtered_videos[12 * page: 12 * (page + 1)]

    if language == "ru":

        return render_template('index.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page,)
    

    elif language == "en":

        return render_template('translate.html', videos=filtered_videos, filter_groups=filter_groups, pages=pages, page=page,)

#---------------------------------------------------------------------------------------------------------------- Login ----------------------------------------------------------------------------------------------------------------

@main.route('/login')
def login():
    
    return render_template('log.html')

#---------------------------------------------------------------------------------------------------------------- Login Check ----------------------------------------------------------------------------------------------------------------

@main.route('/login_check', methods=['POST', 'GET'])
def login_check():

    code = request.form['code']

    if(code==SECRET_CODE):

        return render_template('admin_add.html')
    

    return redirect('/')

#---------------------------------------------------------------------------------------------------------------- Add ----------------------------------------------------------------------------------------------------------------

@main.route('/add', methods=['POST', 'GET'])
def add():

    if(request.form['members_num'].isdigit() and request.form['gender']!=""):

        dict = {}

        url = request.form['url']
        dict['id'] = url[url.find("video/")+6:-1]
        dict['group_name'] = request.form['group_name'].lower()
        dict['members_num'] = int(request.form['members_num'])
        dict['gender'] = request.form['gender']
        dict['video_url'] = "https://rutube.ru/play/embed/"+dict.get('id')
        req = requests.get("https://rutube.ru/api/video/{}/thumbnail/?r...".format(dict.get('id')))
        dict['preview_url'] = req.text[req.text.find("url")+7:-2]
        dict['video_name'] = request.form['video_name'].lower()

        g = str([i for i in dict])[1:-1].replace("'", "")
        v = str([dict.get(i) for i in dict])[1:-1]
        
        if(connect.get_db_status=="postgres"):

            connect.query("insert into elements ({0}) values ({1});".format(g, v))
    

        sqlite = db("sqlite")
        sqlite.query("insert into elements ({0}) values ({1});".format(g, v))
    

    return redirect('/')

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

    url = request.form['url']

    if(url):

        if(connect.get_db_status=="postgres"):

            connect.query("DELETE FROM elements where id = '{0}';".format(url[url.find("video/")+6:-1]))


        sqlite = db("sqlite")
        connect.query("DELETE FROM elements where id = '{0}';".format(url[url.find("video/")+6:-1]))


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