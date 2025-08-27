from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

class StringValidator:
    requiredMessage = 'This is a required field'

    
    def __init__(self):
        self.illegalChars = ["<", ">", "{", "}", ";", ":", "%", '"', "'", ")", "(", "!", "?", "&", "/", "\\", "\"", "#", "*"]
        



    def checkLegal(self, string):
        if string is not None:
            for x in range(0, len(str(string))):
                char = str(string[x])

                for y in range(0, len(self.illegalChars)):
                    if char == self.illegalChars[y]:
                        raise ValidationError(('%(char)s is not allowed'), params={'char': char},)
                    



    #required
    def checkRequiredShortString(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 8: return True
                else: raise ValidationError(('%(string)s cannot be longer than 8 characters'), params={'string': string})
            else: raise ValidationError(('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredMedString(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 16: return True
                else: raise ValidationError(('%(string)s cannot be longer than 16 characters'), params={'string': string})
            else: raise ValidationError(('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredString(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 32: return True
                else: raise ValidationError(('%(string)s cannot be longer than 32 characters'), params={'string': string})
            else: raise ValidationError(('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredLongString(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 64: return True
                else: raise ValidationError(_('%(string)s cannot be longer than 64 characters'), params={'string': string})
            else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredShortSentence(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 128: return True
                else: raise ValidationError(_('%(string)s cannot be longer than 128 characters'), params={'string': string})
            else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredMedSentence(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 256: return True
                else: raise ValidationError(_('%(string)s cannot be longer than 256 characters'), params={'string': string})
            else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredSentence(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 512: return True
                else: raise ValidationError(_('%(string)s cannot be longer than 512 characters'), params={'string': string})
            else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        



    def checkRequiredLongSentence(self, string):
        if string is not None:
            if string != "":
                if len(string) <= 1024: return True
                else: raise ValidationError(_('%(string)s cannot be longer than 1024 characters'), params={'string': string})
            else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})
        else: raise ValidationError(_('%(string)s cannot be blank'), params={'string': string})




    #Optional
    def checkOptionalShortString(self, string):
        if string is not None and string != "":
            if len(string) <= 8: return True
            else: raise ValidationError(('%(string)s cannot be longer than 8 characters'), params={'string': string})
        else: return True
        



    def checkOptionalMedString(self, string):
        if string is not None and string != "":
            if len(string) <= 16: return True
            else: raise ValidationError(('%(string)s cannot be longer than 16 characters'), params={'string': string})
        else: return True
        



    def checkOptionalString(self, string):
        if string is not None and string != "":
            if len(string) <= 32: return True
            else: raise ValidationError(('%(string)s cannot be longer than 32 characters'), params={'string': string})
        else: return True
        



    def checkOptionalLongString(self, string):
        if string is not None and string != "":
            if len(string) <= 64: return True
            else: raise ValidationError(('%(string)s cannot be longer than 64 characters'), params={'string': string})
        else: return True
        



    def checkOptionalShortSentence(self, string):
        if string is not None and  string != "":
            if len(string) <= 128: return True
            else: raise ValidationError(('%(string)s cannot be longer than 128 characters'), params={'string': string})
        else: return True
        



    def checkOptionalMedSentence(self, string):
        if string is not None and string != "":
            if len(string) <= 256: return True
            else: raise ValidationError(('%(string)s cannot be longer than 256 characters'), params={'string': string})
        else: return True
        



    def checkOptionalSentence(self, string):
        if string is not None and string != "":
            if len(string) <= 512: return True
            else: raise ValidationError(('%(string)s cannot be longer than 512 characters'), params={'string': string})
        else: return True
        



    def checkOptionalLongSentence(self, string):
        if string is not None and string != "":
            if len(string) <= 1024: return True
            else: raise ValidationError(('%(string)s cannot be longer than 1024 characters'), params={'string': string})
        else: return True