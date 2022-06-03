import sqlite3 as sql


class ModelDB():

    def __init__(self, dbName):
        self.dbName = dbName
        self.connection = sql.connect(dbName)
        self.cursor = self.connection.cursor()
