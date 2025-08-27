from django.db import models
from django.utils.timezone import now

from user.models import PoliceUser, PublicUser




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

    last_accessed_by = models.ForeignKey(PoliceUser, null = False, blank = False, on_delete = models.DO_NOTHING)
    last_accessed_on = models.DateTimeField('Last Accessed', null = False, blank = True, default = now)


    class Meta:
        db_table = 'document'
        ordering = ('owner', 'issuing_agency', 'document_type', 'document_id')


    def __str__(self): return f'{self.owner} - {self.document_type}: {self.document_id}'