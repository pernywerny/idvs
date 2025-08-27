from django import forms
from __res.__includes.libs.validators.string import StringValidator
from __res.__includes.libs.validators.int import IntegerValidator




strVal = StringValidator()
intVal = IntegerValidator()


class PoliceAuthForm(forms.Form):
    reg_num = forms.CharField(
                                label = 'Regulation Number',
                                required = True,
                                error_messages = {'required': 'Please enter your regulation number to continue'},
                                validators = [strVal.checkLegal, strVal.checkRequiredString],
                                widget = forms.TextInput
                                    (
                                        attrs = {
                                                    'type': 'text',
                                                    'id': 'document',
                                                    'placeholder': 'Reg-15468',
                                                }
                                    )
                            )
    

    password = forms.CharField(
                                label = 'Password', 
								required = True, 
                                error_messages = {'required': 'Please enter your password to continue'}, 
								widget = forms.PasswordInput
									(
										attrs=
										{
										   'class': 'form-control',
                                           'placeholder':'Password',
                                           'type': 'password',
										}
									)
                            )




class CivAuthForm(forms.Form):
    email_addr = forms.EmailField(
                                    label = 'Email Address', 
                                    required = True, 
                                    error_messages = {'required': 'You cannot proceed without entering your email address'},
                                    widget = forms.TextInput
                                        (
                                            attrs =
                                                {
                                                    'class': 'form-control',
                                                    'type': 'text',
                                                    'placeholder':'Email'
                                                }
                                        ),
                                )
    
    

    password = forms.CharField(
                                label = 'Password', 
								required = True, 
                                error_messages = {'required': 'Please enter your password to continue'}, 
								widget = forms.PasswordInput
									(
										attrs=
										{
										   'class': 'form-control',
                                           'placeholder':'Password',
                                           'type': 'password',
										}
									)
                            )

