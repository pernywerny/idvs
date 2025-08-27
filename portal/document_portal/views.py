from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse as HTRes, HttpResponseRedirect as HTRed
from django.template import loader
from django.urls import reverse

from __res.__includes.libs.generators.date import DateTimeGenerator
from __res.__includes.libs.generators.django_messages import MessageController
from __res.__includes.api.main import APILib

from logs.models import AppLog
from user_portal.app_views.police_views import is_logged_in
from .forms import DocumentValidationForm, DocumentSubmissionForm
from .models import Document







gtime = DateTimeGenerator()
msg = MessageController()
app = 'Document Management'
log = AppLog()




def docDash(request):
    now = gtime.getCurrentDatetime
    ip_addr = log.getIP(request)
    action = 'Submitting Document'
    target = None
    error_list = []


    if is_logged_in(request):
        page = loader.get_template('documents/data_pages/document_dashboard.html')
        docs = Document.objects.filter(ver_status = False)
        context = {'docs': docs}
        return HTRes(page.render(context, request))

    else:
        return HTRed(reverse('user_man:auth_pol'))






def addDocument(request):
    now = gtime.getCurrentDatetime
    ip_addr = log.getIP(request)
    action = 'Submitting Document'
    target = None
    error_list = []


    if is_logged_in(request):
        form = DocumentSubmissionForm(request.POST, label_suffix='')
        page = loader.get_template('documents/forms/newDocument.html')
        user = None
        session_id = None

        context = {'form': form}

        if request.method == 'POST':
            if form.is_valid():
                issuing_agency = form.cleaned_data['issuing_agency']
                document_type = form.cleaned_data['document_type']
                document_id = form.cleaned_data['document_id']

                new_doc = Document(
                                    owner_id = 1,
                                    issuing_agency = issuing_agency,
                                    document_type = document_type,
                                    document_id = document_id,
                                    ver_status = False,
                                )
                new_doc.save()

                msg.setSuccessMessage(request, f'Document bearing ID: {document_id} has been sucessfully added')
            
            else:
                for field in form:
                    for error in field.errors:
                        error_inst = f'{field.name}: {error}'
                        error_list.append(error_inst)
                        print(error_list)

        return HTRes(page.render(context, request))

    else:
        return HTRed(reverse('user_man:auth_civ'))






def getDocument(request):
    now = gtime.getCurrentDatetime
    ip_addr = log.getIP(request)
    action = 'Verifying Document'
    target = None
    error_list = []

    if is_logged_in(request):
        form = DocumentValidationForm(request.POST, label_suffix='')
        user = None
        session_id = None

        page = loader.get_template('documents/forms/verificationForm.html')
        context = {'form': form}

        if request.method == 'POST':
            if form.is_valid():
                agency = form.cleaned_data['agency']
                doc_type = form.cleaned_data['doc_type']
                doc_id = form.cleaned_data['doc_id']
                api = APILib()

                try:
                    response = api.verifyDocument(agency.id, doc_type.id, doc_id)
                    ver_status = response['is_verified']
                    
                    if ver_status == True:
                        msg.setSuccessMessage(request, response['message']) 
                        info = response['document_data']
                        document = info['document_id']
                        doc_owner = info['owner_name']

                        

                    else:
                        msg.setErrorMessage(request, response['message'])
                    


                except Exception as exc:
                    msg.exc = exc
                    msg.setErrorMessage(request, msg.exceptionMessage)
                                    

            else:
                for field in form:
                    for error in field.errors:
                        error_inst = f'{field.name}: {error}'
                        error_list.append(error_inst)
                        print(error_list)

        return HTRes(page.render(context, request))


    else:
        return HTRed(reverse('user_man:auth_pol'))