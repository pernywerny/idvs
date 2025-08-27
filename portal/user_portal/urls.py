from django.urls import path
from user_portal.app_views.police_views import authPolice, authCiv, unAuth




app_name = 'user_man'

urlpatterns = [
                    path('auth/police/login', authPolice, name ='auth_pol'),
                    path('auth/public/login', authCiv, name ="auth_civ"),
                    path('auth/logout', unAuth, name ='logout'),
            ]
