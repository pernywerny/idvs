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



    


    
    def generateHashPassword(self, pass_string): #using the pycryptodome library
        if pass_string is not None: #check to ensure the salted string was generated
            bytestring = bytes(pass_string, 'utf-8') #encode the string into bytes
            hash = hash_algo.new() #instantiate new hash object
            hash.update(bytestring) #hash the encoded string
            token = hash.hexdigest() #decode the hashed string from bytes to string

            return token

        else:
            return None

















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



 



        
   


  




    
        

    def formatDate(self, date):
        return date.strftime("%Y-%m-%d")
    



    def convertDTString(self, dt_string): #convert datetime string to datetime object
        if dt_string:
            try:
                dT_obj = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
                return dT_obj
            except Exception as exc: pass
    



   
        








        

