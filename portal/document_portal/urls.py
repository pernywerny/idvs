from django.urls import path
from .views import getDocument, addDocument, docDash




app_name = 'doc_man'


urlpatterns = [
    path('verify-document', getDocument, name ="verify_document"),
    path('new-document', addDocument, name ="new_document"),
    path('', docDash, name ="doc_blank"),
    path('home', docDash, name ='doc_home'),
    path('documents', docDash, name ='all_documents'),
]
