from django.db import models
from django.utils.timezone import now

class PublicUser(models.Model):
    fname = models.CharField('First Name', max_length = 32, null = False, blank = False)
    oth_names = models.CharField('Other Names', max_length = 128, null = False, blank = False)
    lname = models.CharField('Surname', max_length = 64, null = False, blank = False)
    uid = models.CharField('Owner ID', max_length = 32, null = False, blank = True, unique = True)
    passw = models.CharField('Password', max_length = 256, null = False, blank = False, default = 'open12')
    email_addr = models.EmailField('Email Address', max_length = 64, null = True, blank = False)

    added_on = models.DateTimeField('When Added', null = False, blank = True, default = now)


    class Meta:
        db_table = 'pub_user'
        verbose_name = 'Document Owner'
        verbose_name_plural = 'Document Owners'
        ordering = ('fname', 'lname', 'oth_names')


    def __str__(self): return f'{self.fname.title()} {self.oth_names.title()} {self.lname.title()}'




class PoliceUser(models.Model):
    fname = models.CharField('First Name', max_length = 32, null = False, blank = False)
    oth_names = models.CharField('Other Names', max_length = 128, null = False, blank = False)
    lname = models.CharField('Surname', max_length = 64, null = False, blank = False)
    reg_num = models.CharField('Regulation Number', max_length = 32, null = False, blank = False, unique = True)
    passw = models.CharField('Password', max_length = 256, null = False, blank = False, default = 'open12')



    class Meta:
        db_table = 'pol_user'
        verbose_name = 'Police User'
        verbose_name_plural = 'Police Users'
        ordering = ('lname', 'fname', 'reg_num')


    def __str__(self): return f'{self.reg_num} - {self.fname} {self.lname}'
