from django.db import models, connection
from django.utils import timezone

import mysql.connector
from datetime import datetime
from __res.__includes.libs.generators.generate import GenDateTime

gtime = GenDateTime()



class UserLog(models.Model):
    # username = models.CharField('User', max_length = 128, null = False)
    # session_key = models.CharField('Session ID', max_length = 1024, null = False, blank = False)
    # logged_in = models.DateTimeField('User Logged In On', default = timezone.now())
    # logged_out = models.DateTimeField('User Logged Out On', null = True, blank = True)
    # is_active = models.BooleanField('Is Active', default = True)
    # last_active = models.DateTimeField('Last Active', null = True, default = timezone.now())

    class Meta:
        managed = False

    def __init__(self):
        self.db = mysql.connector.connect(
                                        host = '192.168.39.62',
                                        port = 3307,
                                        user = 'foreign_hrDB',
                                        database = 'hrma2',#hrma2
                                        password = 'Open_sesamestreet195',
                                        raise_on_warnings = False,
                                        connect_timeout = 10
                                    )


        self.cursor = self.db.cursor()


    def __str__(self): return f'{self.username}: {self.logged_in} - {self.logged_out}'

    def __del__(self): 
        if self.cursor: self.cursor.close()




    def createSession(self, sesh_key, user):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                                    "insert into user_log(username, session_key, logged_in, logged_out, is_active, last_active) values(%s, %s, %s, %s, %s, %s);",
                                    [user, sesh_key, datetime.now(), None, True, datetime.now()]
                                )
                return True
            # query = '''      
            #             insert into user_log(username, session_key, logged_in, logged_out, is_active, last_active) 
            #             values(%s, %s, %s, %s, %s, %s);
            #         '''
            # vals = (user, sesh_key, datetime.now(), None, True, datetime.now())

            # self.cursor.execute(query, vals)
            # self.db.commit()
            # self.cursor.close()
        except Exception as exc: print(f'Exception ({exc}) while creating userLog.')




    def  getSessionByKey(self, sesh_key):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM user_log WHERE session_key = %s and is_active = %s", [sesh_key, True])
                data = cursor.fetchone()
                return data
            # query = 'SELECT * FROM user_log WHERE session_key = %s;'
            # vals = (sesh_key,)

            # self.cursor.execute(query, vals)
            # data = self.cursor.fetchone()

            # return data
        except Exception as exc: print(f'Exception ({exc}) while retreiving session.')


    

    def getSessionByUser(self, user_id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM user_log WHERE username = %s and is_active = %s", [user_id, True])
                data = cursor.fetchone()
                return data
        except Exception as exc: print(f'Exception ({exc}) while retreiving session.')
        
    


    def resetActiveTime(self, session):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                                "Update user_log SET last_active = %s where session_key = %s and is_active = %s and logged_out = %s limit 1;",
                                [datetime.now(), session, 1, None]
                               )
                return True
            
            # query = "Update user_log SET last_active = %s where session_key = %s and is_active = %s and logged_out = %s limit 1;"
            # vals = (datetime.now(), session, 1, None)

            # self.cursor.execute(query, vals)
            # self.db.commit()
        except Exception as exc: print(f'Exception ({exc}) while setting activity.')




    def handleLogout(self, session):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                                "Update user_log SET logged_out = %s, is_active = %s where session_key = %s and is_active = %s limit 1;",
                                [datetime.now(), 0, session, 1]
                            )
                return True

            # query = "Update user_log SET logged_out = %s, is_active = %s where session_key = %s and is_active = %s limit 1;"
            # vals = (datetime.now(), 0, session, 1)

            # self.cursor.execute(query, vals)
            # self.db.commit()
            # self.cursor.close()
        except Exception as exc: print(f'Exception ({exc}) while logging out.')




    def checkTimeout(self, session, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                                "SELECT last_active FROM user_log WHERE is_active = %s and session_key = %s",
                                [1, session]
                            )
                data_packet = cursor.fetchone()
                
            # query = "SELECT last_active FROM user_log WHERE is_active = %s and session_key = %s"
            # vals = (1, session)
            # self.cursor.execute(query, vals)
            # data_packet = self.cursor.fetchone()
            
            if data_packet:
                last_active = data_packet[0]

                if last_active:
                    interval = gtime.checkTimePassed(last_active)
                    minutes = interval / 60

                    print(last_active)
                    if minutes <= 10: return True
                    else: return None

            else: print('session data could not be found')
        except Exception as exc: print(f'Exception ({exc}) while checking time.')




    # def checkTime






  
