import pymysql
import requests

class Connectmysql():

    def __init__(self, db_info, database="litemall"):

        self.db = pymysql.connect( database=database, **db_info
        )
        self.cursor = self.db.cursor()

    def sql_select(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def sql_execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    def close(self):
        self.db.close()
