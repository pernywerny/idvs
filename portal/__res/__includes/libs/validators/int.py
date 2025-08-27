from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class IntegerValidator:
    def __init__(self) -> None:
        self.max_val = None
        self.min_val = None



    def checkInt(self, val):
        try:
            if isinstance(int(val), int):
                return True
        except: pass


    def validateInt(self, num_input):
        if num_input and self.max_val and self.min_val:
            if self.checkInt(num_input) == True:
                if num_input <= self.max_val and num_input >= self.min_val:
                    return True
                

    def validateRequiredInput(self, num):
        if num and num is not None:
            if self.checkInt(num):
                return True
            else: raise ValidationError('must be a number')
        else: raise ValidationError('cannot be blank')


    def validateOptionalInput(self, num):
        if num and num is not None:
            if self.checkInt(num): return True
            else: raise ValidationError('must be a number')
        else: return True