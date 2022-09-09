from django.urls import path
from .logoutview import logout_user
from .views import showLoginPage, dologin

urlpatterns = [
    path('logout_user/', logout_user, name='logout'),
    path('',showLoginPage,name="showlogin"),
    path('dologin',dologin,name="dologin"),
]