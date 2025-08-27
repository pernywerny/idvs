import time
import pytz
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class DateTimeGenerator:
    def __init__(self):
        self.tZ = pytz.timezone('America/Guyana')
        self.datetime_obj = datetime.now()
        self.adult_age = 18
        self.reg_retirement_age = 55
        self.sc_retirement_age = 65



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



    def getCurrentAge(self, dob):
        cur_date = date.today()

        if cur_date:
            age_years = cur_date.year - dob.year
            age_months = cur_date.month - dob.month
            return f'{age_years} years {age_months} months'



        
    def calculateRetirementYear(self, dob, designation):
        try:
            if designation == 2:
                age_years = dob.year + self.reg_retirement_age
                
            elif designation == 7 or designation == 3 or designation == 6:
                age_years = dob.year + self.sc_retirement_age

            else:
                age_years = 'Not Applicable'

            return age_years
        except:
            pass



    def getAdultYear(self):
        cur_year = int(self.getCurrentYear())

        if cur_year:
            adult_year = cur_year - self.adult_age
            return adult_year

    

    def getRetirementYear(self):
        cur_year = int(self.getCurrentYear())

        if cur_year:
            ret_year = cur_year - self.reg_retirement_age
            return ret_year




    def getDateDifferenceDays(self, date1, date2):
        try:
            days = time.mktime(date1.timetuple()) - time.mktime(date2.timetuple())
            return days
        except:
            return None
        

    def formatDate(self, date):
        return date.strftime("%Y-%m-%d")
    



    def checkMinutesPassed(self, dt_obj):
        if dt_obj:
            try:
                now = datetime.now()

                if dt_obj:
                    interval = now - dt_obj
                    return interval

            except Exception as exc: pass