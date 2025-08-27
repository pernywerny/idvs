import time
import pytz
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class DateTimeGenerator:
    def __init__(self):
        self.tZ = pytz.timezone('America/Guyana')
        self.datetime_obj = datetime.now()
   



    def getCurrentDatetime(self):
        return self.datetime_obj
    

    def getCurrentTime(self):
        time = self.datetime_obj.time()
        return time



    def getCurrentDate(self):
        date = self.datetime_obj.date()
        return date


    def getCurrentYear(self):
        year = self.datetime_obj.year
        return year






    
        

    def formatDate(self, date):
        return date.strftime("%Y-%m-%d")
    



   