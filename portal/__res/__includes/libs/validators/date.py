from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

import datetime

from libs.generators.date import DateTimeGenerator


class DateTimeValidator:

    gtime = DateTimeGenerator()
    now = gtime.getCurrentDatetime()
    cur_date = gtime.getCurrentDate()


    def dateChecker(self, date):
        if isinstance(date, datetime.date):
                date_diff = date - self.cur_date
                diff_days = int(date_diff.days)
                
                if diff_days > 0: return True
                elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the past')
                elif diff_days == 0: raise ValidationError('Error: date entered cannot be today.')
                else: raise ValidationError('Invalid Date')
        else: raise ValidationError('Only Dates can be entered')




    def dateCheckerInc(self, date):
        if isinstance(date, datetime.date):
                date_diff = date - self.cur_date
                diff_days = int(date_diff.days)
                
                if diff_days >= 0: return True
                elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the past')
                else: raise ValidationError('Invalid Date')
        else: raise ValidationError('Only Dates can be entered')




    def dateCheckerOptional(self, date):
        if date is not None:
            if date and len(str(date)) > 4:
                try:
                    date_diff = date - self.cur_date
                    diff_days = int(date_diff.days)
                    
                    if diff_days > 0: return True
                    elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the past')
                    elif diff_days == 0: return True
                    else: raise ValidationError('Invalid Date')

                except Exception as exc: raise ValidationError(f'Date checking failed with error: {exc}')
        else: return True




    def dateCheckerOptionalInc(self, date):
        if date is not None:
            if date and len(str(date)) > 4:
                try:
                    date_diff = date - self.cur_date
                    diff_days = int(date_diff.days)
                    
                    if diff_days >= 0: return True
                    elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the past')
                    else: raise ValidationError('Invalid Date')

                except Exception as exc: raise ValidationError(f'Date checking failed with error: {exc}')
        else: return True





    def dateCheckerPast(self, date):
        if isinstance(date, datetime.date):
                date_diff = self.cur_date - date
                diff_days = int(date_diff.days)
                
                if diff_days > 0: return True
                elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the future. {date} is invalid')
                elif diff_days == 0: raise ValidationError('Error: date entered cannot be Today.')
                else: raise ValidationError('Invalid Date')
        else: raise ValidationError(f'Only Dates can be entered. {date} is not valid')




    def dateCheckerPastInc(self, date):
        if isinstance(date, datetime.date):
                date_diff = self.cur_date - date
                diff_days = int(date_diff.days)
                
                if diff_days >= 0: return True
                elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the future')
                else: raise ValidationError('Invalid Date')
        else: raise ValidationError('Only Dates can be entered')




    def dateCheckerPastOptional(self, date):
        if date is not None:
            if date and len(str(date)) > 4:
                try:
                    date_diff = self.cur_date - date
                    diff_days = int(date_diff.days)
                
                    if diff_days > 0: return True
                    elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the future')
                    elif diff_days == 0: raise ValidationError('Error: date entered cannot be today.')
                    else: raise ValidationError('Invalid Date')
                except:
                    pass
        else: return True



    
    def dateCheckerPastOptionalInc(self, date):
        if date is not None:
            if date and len(str(date)) > 4:
                try:
                    date_diff = self.cur_date - date
                    diff_days = int(date_diff.days)
                
                    if diff_days >= 0: return True
                    elif diff_days < 0: raise ValidationError(f'Error: date entered is ({diff_days * -1} days) in the future')
                    else: raise ValidationError('Invalid Date')
                except:
                    pass
        else: return True




