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
                id SERIAL PRIMARY KEY,
                group_name TEXT,
                members_num TEXT,
                gender TEXT,
                url TEXT,
                preview TEXT
            )
        """)


    def create(self, table_name):
        self.query("CREATE TABLE IF NOT EXISTS "+table_name+""" (
                id SERIAL PRIMARY KEY,
                group_name TEXT,
                members_num TEXT,
                gender TEXT,
                url TEXT,
                preview TEXT
            )
        """)