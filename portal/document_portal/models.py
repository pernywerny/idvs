from django.db import models
from user_portal.models import *
from django.utils.timezone import now



class Agency(models.Model):
    name = models.CharField('Agency Name', max_length = 128, null = False, blank = False, unique = True)
    address = models.CharField('Agency Address', max_length = 256, null = True, blank = True)

    class Meta:
        db_table = 'agency'
        ordering = ('name',)


    def __str__(self): return self.name.title()
    



class DocumentType(models.Model):
    doc_type = models.CharField('Document Type', null = False, blank = False, unique = True, max_length = 128)

    class Meta:
        db_table = 'doc_type'


    def __str__(self): return self.doc_type.title()




class Document(models.Model):
    owner = models.ForeignKey(PublicUser, null = False, blank = False, on_delete = models.CASCADE)
    issuing_agency = models.ForeignKey(Agency, null = False, blank = False, on_delete = models.PROTECT)
    document_type = models.ForeignKey(DocumentType, null = False, blank = False, on_delete = models.PROTECT)
    document_id = models.CharField('Document ID', null = False, blank = False, max_length = 64)

    ver_status = models.BooleanField('Is Verified', null = False, blank = True, default = False)
    verified_by = models.ForeignKey(PoliceUser, null = True, blank = False, on_delete=models.PROTECT)
    verified_on = models.DateTimeField('When Verified', null = True, blank = True, default = now)
    date_submitted = models.DateTimeField('When Submitted', null = False, blank = False, default = now)


    class Meta:
        db_table = 'ver_document'


    def __str__(self): return f'{self.owner} - {self.document_type}: {self.document_id} -- {self.ver_status}'
