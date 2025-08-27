from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy



class EmailValidator:
    def checkEmail(self, email):
        if email is not None:
            if len(email) < 32 and len(email) > 5:
                if email.find("@") > 0:
                    if email.find(".com") > 1:
                        if (
                            email.find("@gmail.com") > 1
                            or email.find("@yahoo.com") > 1
                            or email.find("@icloud.com") > 1
                        ):
                            return True
                    else: raise ValidationError('Only GMail, Yahoo, or iCloud accounts allowed')
                else: raise ValidationError('Invalid Email Address')
            else: raise ValidationError('Invalid Length')
        else: raise ValidationError('Email cannot be blank')
                