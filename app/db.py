import psycopg2
from config import *

class db:

    def __init__(self, dbName):

        self.connection = psycopg2.connect(
            dbname=dbName,
            user=DATABASE_LOGIN,
            password=DATABASE_PASSWORD,
            host="localhost",
            port="5432"
        )     
        self.dbName = dbName


    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()


    def select(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()


    def drop_create(self, table_name):
        self.query("DROP TABLE IF EXISTS "+table_name+";")
        self.query("CREATE TABLE IF NOT EXISTS "+table_name+""" (
	        id TEXT NOT NULL,
	        group_name TEXT NOT NULL,
	        members_num INTEGER NOT NULL,
	        gender TEXT NOT NULL,
	        video_url TEXT NOT NULL,
	        preview_url TEXT NOT NULL,
	        video_name TEXT NOT NULL,
	        CONSTRAINT elements_pk PRIMARY KEY (id)
        );
        """)


    def create(self, table_name):
        self.query("CREATE TABLE IF NOT EXISTS "+table_name+""" (
	        id TEXT NOT NULL,
	        group_name TEXT NOT NULL,
	        members_num INTEGER NOT NULL,
	        gender TEXT NOT NULL,
	        video_url TEXT NOT NULL,
	        preview_url TEXT NOT NULL,
	        video_name TEXT NOT NULL,
	        CONSTRAINT elements_pk PRIMARY KEY (id)
        );
        """)