import psycopg2
from config import *
import sqlite3

def postgres_connect():

    return psycopg2.connect(
        dbname="postgres",
        user=DATABASE_LOGIN,
        password=DATABASE_PASSWORD,
        host="localhost",
        port="5432"
    )


class db:

    def __init__(self, selectDatabase="postgres"):
        
        if(selectDatabase=="postgres"):

            try:
            
                self.connection = postgres_connect()
                self.db_status = "postgres"
                self.cursor = self.connection.cursor()
            
            except:     
                
                print("Can't connect to Postgres.")
                self.forced_connect()
                

        elif(selectDatabase=="sqlite"):
            
            self.forced_connect()


    def forced_connect(self):
                    
        try:
                
            self.connection = sqlite3.connect("app/old_db/horeo.db", check_same_thread=False)
            self.db_status = "sqlite"
            self.cursor = self.connection.cursor()

            
        except:

            print("Can't connect to SQLite.")


    def get_db_status(self):

        return self.db_status
    

    def query(self, query):

        self.cursor.execute(query)
        self.connection.commit()


    def select(self, query):

        self.cursor.execute(query)
        return self.cursor.fetchall()


    def drop(self, table_name):
        
        self.query("DROP TABLE IF EXISTS "+table_name+";")


    def drop_create(self, table_name):

        self.drop(table_name)
        self.create(table_name)

    def close(self):

        self.connection.close()


    def create(self, table_name):

        self.query("CREATE TABLE IF NOT EXISTS "+table_name+""" (
	        id TEXT NOT NULL,
	        group_name TEXT NOT NULL,
	        members_num INTEGER NOT NULL,
	        gender TEXT NOT NULL,
	        embed_url TEXT NOT NULL,
	        preview_url TEXT NOT NULL,
	        video_name TEXT NOT NULL,
            video_url TEXT NOT NULL,
	        CONSTRAINT elements_pk PRIMARY KEY (id)
        );
        """)