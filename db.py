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


    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()