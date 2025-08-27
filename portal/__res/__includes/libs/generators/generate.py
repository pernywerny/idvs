import random
from Crypto.Hash import SHA3_512 as hash_algo
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from random import randint
import time
import pytz

class KeyGenerator:

    def __init__(self) -> None:
        self.charLib1 = "qw45ertyuiopAS1DFGHJK7LzxcvbnmPOIUYTREW389QMNBVCXZ026"
        self.charLib2 = "_@#&%*!><?+-$"
        self.charLib3 = "1234567890"


    def generateShortToken(self):
        list_lib = list(self.charLib1)
        blank_string = ""
        random.shuffle(list_lib)
        shuffled_string = blank_string.join(list_lib)
        token = shuffled_string[0:6]
        return token


    
    def generateLongToken(self):
        list_lib = list(self.charLib1)
        blank_string = ""
        random.shuffle(list_lib)
        shuffled_string = blank_string.join(list_lib)
        token = shuffled_string[0:12]
        return token




    def genNToken(self, n):
        if n > 0:
            lib = self.charLib3 + self.charLib1 + self.charLib2
            list_lib = list(lib)
            blank_string = ""
            random.shuffle(list_lib)
            shuffled_string = blank_string.join(list_lib)
            strlen = len(shuffled_string)
            random_length = randint(int(8),int(strlen))

            if n <= strlen:
                token = shuffled_string[0:n]

            token = shuffled_string[0:random_length]

            return token

        else:
            return None



    def generatePasswordString(self, password, email): #method to generate a salted string
        joined_string = self.charLib3 + self.charLib1 + self.charLib2 #concat the different char library strings
        start = len(password)
        end = len(email)
        total = len(joined_string)

        
        #Below a salt would be generated which uses the length of the email to determine the characters that would be used from the 
        #char libs provided that len(email) is not greater than the len(joined char libs) and greater that the len(password)
        #otherwise return a standard salted string
        if start < end: 
            if end < total:
                key_string = email + joined_string[0:end] + password
            
            elif end > total:
                if start < total:
                    key_string = email + joined_string[0:start] + password
                
                else:
                    key_string = email + joined_string[0:13] + password

            else:
               key_string = email + joined_string[0:10] + password 



        #Below a salt would be generated which uses the length of the email to determine the characters that would be used from the 
        #char libs provided that len(password) is not greater than the len(joined char libs) and greater that the len(email)
        #otherwise return a standard salted string
        elif start > end:
            if start < total:
                key_string = email + joined_string[0:start] + password

            elif start > total:
                if end < total:
                    key_string = email + joined_string[0:end] + password
                
                else:
                    key_string = email + joined_string[0:11] + password

            else:
                key_string = email + joined_string[0:20] + password



        #if the len(email) is the same as the len(password) then this will happen
        elif start == end:
            end = end + 12

            if end < total:
                key_string = email + joined_string[0:end] + password
            
            else:
                key_string = email + joined_string[0:19] + password



        #if none of those characters work, then return *None* which will cause the password generation to fail
        else:
            key_string = None

        
        return key_string


    
    def generateHashPassword(self, pass_string): #using the pycryptodome library
        if pass_string is not None: #check to ensure the salted string was generated
            bytestring = bytes(pass_string, 'utf-8') #encode the string into bytes
            hash = hash_algo.new() #instantiate new hash object
            hash.update(bytestring) #hash the encoded string
            token = hash.hexdigest() #decode the hashed string from bytes to string

            return token

        else:
            return None




    def getNextIdInQueue(self, qid):
        if qid > 1:
            prev = qid - 1

        else:
            prev = 1

        return prev




    # def get














class GenDateTime:

    def __init__(self):
        self.tZ = pytz.timezone('America/Guyana')
        self.datetime_obj = datetime.now()
        self.adult_age = 17
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
    



    def convertDTString(self, dt_string): #convert datetime string to datetime object
        if dt_string:
            try:
                dT_obj = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
                return dT_obj
            except Exception as exc: pass
    



    def checkTimePassed(self, dt_obj): #returns time_passed in seconds taking a datetime object as param 
        if dt_obj:
            try:
                now = datetime.now()

                if dt_obj:
                    interval = now - dt_obj
                    seconds = interval.total_seconds()
                    return seconds

            except Exception as exc: pass
        








        

