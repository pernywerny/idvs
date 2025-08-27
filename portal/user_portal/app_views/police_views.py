from django.shortcuts import render, redirect
from django.http import HttpResponse as HTRes, HttpResponseRedirect as HTRed
from django.template import loader
from django.urls import reverse


from __res.__includes.libs.generators.date import DateTimeGenerator
from __res.__includes.libs.generators.django_messages import MessageController

from logs.models import AppLog
from user_portal.forms import PoliceAuthForm, CivAuthForm
from user_portal.models import PoliceUser, PublicUser




gtime = DateTimeGenerator()
msg = MessageController()
app = 'User Management'
log = AppLog()






def is_logged_in(request):
    if request.session.has_key('who'):
        if request.session.has_key('user_type'):
            if request.session.has_key('id'):
                if request.session.has_key('is_logged_in') and request.session['is_logged_in'] == True:
                    return True
                



def unAuth(request):
    if is_logged_in(request):
        del request.session['who']
        del request.session['user_type']
        del request.session['id']
        del request.session['is_logged_in']

        return HTRed(reverse('doc_man:doc_home'))







def authPolice(request):
    now = gtime.getCurrentDatetime
    ip_addr = log.getIP(request)
    action = 'Submitting Document'
    target = None
    error_list = []


    if not is_logged_in(request):
        page = loader.get_template('user/account/login.html')
        form = PoliceAuthForm(request.POST, label_suffix='')
        mode = 'Police'
        context = {'form': form, 'type': mode, 'header': 'Police Login'}


        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['reg_num']
                passw = form.cleaned_data['password']
                hashed_pass = passw

                try: user = PoliceUser.objects.get(passw = hashed_pass, reg_num = username)
                except: user = None

                if user:
                    request.session['is_logged_in'] = True
                    request.session['who'] = f"{user.lname}"
                    request.session['user_type'] = mode
                    request.session['id'] = user.reg_num

                    msg.setSuccessMessage(request, 'Successfully logged in')
                    return HTRed(reverse('doc_man:doc_home'))

                else:
                    msg.setErrorMessage(request, 'Incorrect regulation number or password entered')

            else:
                for field in form:
                    for error in field.errors:
                        error_inst = f'{field.name}: {error}'
                        error_list.append(error_inst)
                        print(error_list)

        return HTRes(page.render(context, request))

    else:
        return HTRed(reverse('doc_man:doc_home'))
    




def authCiv(request):
    now = gtime.getCurrentDatetime
    ip_addr = log.getIP(request)
    action = 'Submitting Document'
    target = None
    error_list = []


    if not is_logged_in(request):
        page = loader.get_template('user/account/login.html')
        form = CivAuthForm(request.POST, label_suffix='')
        mode = 'Civilian'
        context = {'form': form, 'type': mode, 'header': 'Public Login'}


        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data['email_addr']
                passw = form.cleaned_data['password']
                hashed_pass = passw

                user = PublicUser.objects.filter(passw = hashed_pass, email_addr = username)

                if user:
                    request.session['is_logged_in'] = True
                    request.session['who'] = f"{user.fname} {user.lname}"
                    request.session['user_type'] = mode
                    request.session['id'] = user.uid

                    msg.setSuccessMessage(request, 'Successfully logged in')
                    return HTRed(reverse('doc_man:doc_home'))

                else:
                    msg.setErrorMessage(request, 'Incorrect regulation number or password entered')

            else:
                for field in form:
                    for error in field.errors:
                        error_inst = f'{field.name}: {error}'
                        error_list.append(error_inst)
                        print(error_list)

        return HTRes(page.render(context, request))

    else:
        return HTRed(reverse('doc_man:doc_home'))