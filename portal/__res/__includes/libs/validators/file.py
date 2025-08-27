from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


class FileValidator:
    def __init__(self):        
        self.banned_extensions = ['php', 'py', 'c', 'js', 'html', 'css', 'asp', 'bat', 'txt', 'sql']


    def getExtension(self, filename): # Get file extension
        if filename:
            if filename is not None and filename != '':
                ext = str(filename).split('.')
                return ext[1]

         
            

    def fileExists(self, file):
        if file:
            if file is not None and file != '':
                return True




    def checkDangerous(self, filename): # check for dangerous filetypes
        ext = self.getExtension(filename)

        if ext:
            if ext != '':
                for i in self.banned_extensions:
                    if i == ext:
                        raise ValidationError('Invalid file type')
                    else: return True
            else: raise ValidationError('File not Found')
        else: raise ValidationError('File extension not found')




    def isPDF(self, filename): #Check if file is a PDF
        if self.fileExists(self):
            if self.getExtension(filename) == 'pdf': return True
            else: raise ValidationError(' must be a PDF')
        else: raise ValidationError('Error File not uploaded')