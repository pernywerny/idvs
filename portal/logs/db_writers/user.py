import csv
import os
import pandas as pan
from datetime import datetime

from libs.generate import GenDateTime

gtime = GenDateTime()


class UserLog:
    def __init__(self):
        self.base_dir = os.getcwd()
        self.sessionFile = 'session_data.csv'
        self.sessionFilePath = f'{str(self.base_dir)}/media/logs/{self.sessionFile}'
        self.fieldList = ['id', 'username', 'session_key', 'logged_in', 'logged_out', 'is_active', 'last_active']




    def getSessionData(self):
        try:
            data_list = []

            with open(self.sessionFilePath, mode ='r') as data_file:
                csv_reader = csv.DictReader(data_file)

                for row in csv_reader:
                    data_list.append(row)

            return data_list

        except Exception as exc: pass




    def setSessionData(self, session, user):
        try:
            if session and user:
                now = gtime.getCurrentDatetime()
                user_data = {
                                'id': 1, 'username': user,
                                'session_key': session, 'logged_in': now, 'logged_out': None,
                                'is_active': 1, 'last_active': now
                            }
                
                with open(self.sessionFilePath, 'at') as data_file:
                    csv_writer = csv.DictWriter(data_file, fieldnames = self.fieldList) #create the dictionary writer object

                    #csv_writer.writeheader() #write dict header
                    csv_writer.writerow(user_data)


        except Exception as exc: pass





    def resetActiveTime(self, session):
        try:
            if os.path.exists(self.sessionFilePath) and session:
                sesh_file = pan.read_csv(self.sessionFilePath, encoding ="cp1252")
                
                if sesh_file is not None:
                    for i in sesh_file.index:
                        sesh_key = sesh_file.loc[i, 'session_key']
                        datetime_obj = datetime.now()
                        # last = sesh_file.loc[i, 'last_active']

                        if session == sesh_key:
                            sesh_file.loc[i, 'last_active'] = datetime_obj
                            sesh_file.to_csv(self.sessionFilePath, index = False)

        except Exception as exc: pass




    def handleLogout(self, session):
        try:
            if os.path.exists(self.sessionFilePath) and session:
                sesh_file = pan.read_csv(self.sessionFilePath, encoding ="cp1252")

                if sesh_file is not None:
                    for i in sesh_file.index:
                        sesh_key = sesh_file.loc[i, 'session_key']
                        datetime_obj = datetime.now()
                        act_status = sesh_file.loc[i, 'is_active']

                        if session == sesh_key:
                            if act_status == 1:
                                sesh_file.loc[i, 'last_active'] = datetime_obj
                                sesh_file.loc[i, 'logged_out'] = datetime_obj
                                sesh_file.loc[i, 'is_active'] = 0
                                sesh_file.to_csv(self.sessionFilePath, index = False)

        except Exception as exc: pass
