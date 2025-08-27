from django.shortcuts import render
from .userLogs import UserLog

from libs.generate import GenDateTime
from hr_main.views import isAuth, getUsername, is_logged_in

gtime = GenDateTime()

def endSession(request):
    if isAuth(request):
        try:
            sesh_key = request.session['sesh_id']
            now = gtime.getCurrentDatetime()
            session = UserLog.objects.get(session = sesh_key, is_active = True)

            session.logged_out = now
            session.is_active = False
            session.last_active = now
            session.save()

        except Exception as exc: pass




def setActiveTime(request):
    if is_logged_in(request):
        pass



def newSession(request):
    if is_logged_in(request):
        try:
            sesh_key = request.session['sesh_id']
            now = gtime.getCurrentDatetime()
            user = getUsername(request)
            
            session = UserLog(
                                session = sesh_key,
                                username = user,
                                logged_in = now,
                                last_active = now,
                                is_active = True
                            )

            session.save()


        except Exception as exc:
            print(exc)
