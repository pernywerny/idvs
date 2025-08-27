from django.db import models
from django.utils import timezone

import mysql.connector
from datetime import datetime
from libs.generate import GenDateTime

gtime = GenDateTime()



class UserLog(models.Model):
    # username = models.CharField('User', max_length = 128, null = False)
    # session_key = models.CharField('Session ID', max_length = 1024, null = False, blank = False)
    # logged_in = models.DateTimeField('User Logged In On', default = timezone.now())
    # logged_out = models.DateTimeField('User Logged Out On', null = True, blank = True)
    # is_active = models.BooleanField('Is Active', default = True)
    # last_active = models.DateTimeField('Last Active', null = True, default = timezone.now())

    db = mysql.connector.connect(
                                    host = '192.168.39.62',
                                    port = 3307,
                                    user = 'foreign_hrDB',
                                    database = 'hrma2',#hrma2
                                    password = 'Open_sesamestreet195',
                                )


    cursor = db.cursor()


    def __str__(self): return f'{self.username}: {self.logged_in} - {self.logged_out}'




    def createSession(self, sesh_key, user):
        try:
            cursor = self.db.cursor()
            query = '''      
                        insert into user_log(username, session_key, logged_in, logged_out, is_active, last_active) 
                        values(%s, %s, %s, %s, %s, %s);
                    '''
            vals = (user, sesh_key, datetime.now(), None, True, datetime.now())

            cursor.execute(query, vals)
            self.db.commit()
            cursor.close()
        except Exception as exc: print(f'Exception ({exc}) while creating userLog.')




    def getSessionByKey(self, sesh_key):
        try:
            cursor = self.db.cursor()
            query = 'SELECT * FROM user_log WHERE session_key = %s;'
            vals = (sesh_key,)

            cursor.execute(query, vals)
            data = cursor.fetchone()

            cursor.close()

            return data
        except Exception as exc: print(f'Exception ({exc}) while retreiving session.')
        
    


    def resetActiveTime(self, session):
        try:
            cursor = self.db.cursor()
            query = "Update user_log SET last_active = %s where session_key = %s limit 1;"
            vals = (datetime.now(), session)

            cursor.execute(query, vals)
            self.db.commit()
            cursor.close()
        except Exception as exc: print(f'Exception ({exc}) while setting activity.')




    def handleLogout(self, session):
        try:
            cursor = self.db.cursor()
            query = "Update user_log SET logged_out = %s, is_active = %s where session_key = %s and is_active = %s limit 1;"
            vals = (datetime.now(), 0, session, 1)

            cursor.execute(query, vals)
            self.db.commit()
            cursor.close()
        except Exception as exc: print(f'Exception ({exc}) while logging out.')




    def checkTimeout(self, session, request):
        try:
            cursor = self.db.cursor()
            query = "SELECT last_active FROM user_log WHERE is_active = %s and session_key = %s"
            vals = (1, session)
            cursor.execute(query, vals)
            data_packet = cursor.fetchone()

            cursor.close()

            if data_packet:
                last_active = data_packet[0]

                if last_active:
                    interval = gtime.checkTimePassed(last_active)
                    minutes = interval / 60

                    if minutes <= 10:
                        return True
        except Exception as exc: print(f'Exception ({exc}) while checking time.')






  
