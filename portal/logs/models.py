from django.db import models
import mysql.connector

from .userLogs import UserLog

# Create your models here.
class AppLog(models.Model):
    log_id = models.BigAutoField(primary_key = True)
    action_taken = models.CharField(max_length = 499)
    log_type = models.CharField(max_length = 16)
    user = models.CharField(max_length = 128)
    when_done = models.DateTimeField()
    log_session_id = models.CharField(max_length = 255)
    mac_address = models.CharField(max_length = 32)
    update_s = 'Update-Success'
    update_f = 'Update-Failure'
    read_s = 'Read-Success'
    read_f = 'Read-Failure'
    create_f = 'Create-Failure'
    create_s = 'Create-Success'
    auth_f = 'Authentication-Failure'
    auth_s = 'Authentication-Success'
    alert_string = 'Illegal Operation'
    alert_process = 'Potentially Illegal Operation'
    validate_f = 'Validation Failed'
    upload_f = 'File Upload Failed'
    upload_s = 'File Upload Passed'
    exception = 'Exception Thrown'
    blank_session = 'session_not_set'
    

    class Meta:
        managed = False
        db_table = 'app_log'
        ordering = ['log_session_id']


    def __str__(self):
        return f'{self.user} - {self.log_session_id}'

    
    def makeLog(self, action, l_type, user, when, session):
        #connect to database
        db = mysql.connector.connect(
                                        host = '192.168.39.62',
                                        port = 3307,
                                        user = 'foreign_hrDB',
                                        database = 'hrma2',#hrma2
                                        password = 'Open_sesamestreet195',
                                    )
        

        cursor = db.cursor()
        query = 'insert into app_log(action_taken, log_type, user, when_done, log_session_id) values(%s, %s, %s, %s, %s)'
        log_values = (action, l_type, user, when, session)
        cursor.execute(query, log_values)
        db.commit()




    def newLog(self, action, log_type, log_user, when, app, session, ip, target):
        db = mysql.connector.connect(
                                        host = '192.168.39.62',
                                        port = 3307,
                                        user = 'foreign_hrDB',
                                        database = 'hrma2',#hrma2
                                        password = 'Open_sesamestreet195',
                                    )
        
        cursor = db.cursor()
        query = '''
                    insert into hr_log(log_action, log_type, log_user, action_dt, app, sesh_id, ip_addr, target_pk) 
                    values(%s, %s, %s, %s, %s, %s, %s, %s)
                '''
        
        log_values = (action, log_type, log_user, when, app, session, ip, target)
        cursor.execute(query, log_values)
        db.commit()






    def getIP(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    



