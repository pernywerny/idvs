from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

from .string import StringValidator
from .int import IntegerValidator


class InformationValidator(StringValidator, IntegerValidator):
    def validateVotersID(self, doc_id):
        if self.checkLegal(str(doc_id)):
            if self.checkInt(doc_id):
                if len(str(doc_id)) == 9: return True
                else: raise ValidationError('Invalid Length')
            else: raise ValidationError('Number was not entered')
        else: raise ValidationError('Invalid characters entered')



    def validateNisID(self, doc_id):
        if self.checkRequiredString(doc_id):
            if self.checkLegal(doc_id):
                if len(doc_id) <= 10: return True
                else: raise ValidationError('Invalid Length')



    def validatePassportID(self, doc_id):
        if self.checkRequiredString(doc_id):
            if self.checkLegal(doc_id):
                if len(doc_id) > 8 and len(doc_id) < 16: return True
                else: raise ValidationError('Invalid Length')
            else: raise ValidationError('Invalid characters entered')
        return True



    def validateTinID(self, doc_id):
        if self.checkInt(doc_id):
            if len(str(doc_id)) >= 8 and len(str(doc_id)) < 16: return True
            else: raise ValidationError('Invalid Length')
        else: raise ValidationError('T.I.N must be a number')
        