from django import forms
from __res.__includes.libs.validators.string import StringValidator
from __res.__includes.libs.validators.int import IntegerValidator
from .models import *




strVal = StringValidator()
intVal = IntegerValidator()



class DocumentValidationForm(forms.Form):
    agency = forms.ModelChoiceField(
                                            queryset = Agency.objects.all(),
                                            empty_label = 'Select subject agency',
                                            label = 'Agency',
                                            required = True,
                                            error_messages = {'required': 'This is a required field'},
                                            widget = forms.Select
                                                (
                                                    attrs = {
                                                                'class': 'form-control',
                                                                'label': 'Agency Name',
                                                                'id': 'agency',
                                                            }
                                                )
                                        )
    
    doc_type = forms.ModelChoiceField(
                                            queryset = DocumentType.objects.all(),
                                            empty_label = 'Select document type',
                                            required = True,
                                            widget = forms.Select
                                                (
                                                    attrs = {
                                                                'class': 'form-control',
                                                                'label': 'Document Type',
                                                                'id': 'type',
                                                            }
                                                )
                                        )
    
    doc_id = forms.CharField(
                                label = 'Document ID',
                                required = True,
                                validators = [strVal.checkLegal, strVal.checkRequiredString],
                                widget = forms.TextInput
                                    (
                                        attrs = {
                                                    'type': 'text',
                                                    'id': 'document',
                                                }
                                    )
                            )
    




class DocumentSubmissionForm(forms.ModelForm):
    issuing_agency = forms.ModelChoiceField(
                                            queryset = Agency.objects.all(),
                                            empty_label = 'Select subject agency',
                                            label = 'Agency',
                                            required = True,
                                            error_messages = {'required': 'This is a required field'},
                                            widget = forms.Select
                                                (
                                                    attrs = {
                                                                'class': 'form-control',
                                                                'label': 'Agency Name',
                                                                'id': 'agency',
                                                            }
                                                )
                                        )
    



    document_type = forms.ModelChoiceField(
                                            queryset = DocumentType.objects.all(),
                                            empty_label = 'Select document type',
                                            required = True,
                                            widget = forms.Select
                                                (
                                                    attrs = {
                                                                'class': 'form-control',
                                                                'label': 'Document Type',
                                                                'id': 'type',
                                                            }
                                                )
                                        )
    
    document_id = forms.CharField(
                                label = 'Document ID',
                                required = True,
                                validators = [strVal.checkLegal, strVal.checkRequiredString],
                                widget = forms.TextInput
                                    (
                                        attrs = {
                                                    'type': 'text',
                                                    'id': 'document',
                                                }
                                    )
                            )
    

    class Meta:
        exclude = ['owner', 'ver_status', 'verified_by', 'verified_on']
        model = Document