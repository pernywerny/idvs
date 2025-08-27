import mysql.connector as conn
from datetime import *
from dateutil.relativedelta import *
import pytz

class Log:
    def __init__(self, host, database):
        self.db_name = database
        self.db_host = host
        self.timezone = pytz.timezone("America/Guyana")



    def connect(self):
        username = 'foreign'
        password = None
        connection = conn.connect(
                                    host = self.db_host, 
                                    user = username, 
                                    password = password, 
                                    database = self.db_name
                                )
        return connection
    



    def makeLog(self, db_table, user, ip, action, status):
        if user and action:
            now = datetime.datetime.now(tz=self.timezone)

            query = '''
                        INSERT INTO %s(user, client_ip, user_action, date_done, success_status)
                        VALUES(%s, %s, %s, %s, %s)
                    '''
            vals = (db_table, user, ip, action, now, status)

            dbCon = self.connect()
            dbCursor = dbCon.cursor()

            dbCursor.execute(query, vals)
            dbCon.commit()