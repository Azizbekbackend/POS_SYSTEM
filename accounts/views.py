from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .UserBackEnd import UserBackEnd
from django.contrib.auth import login
from django.urls import reverse


# Create your views here.



def showLoginPage(request):
    return render(request, 'login_page.html')


def dologin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Ruxsat berilmagan so'rov</h2>")
    else:
        user=UserBackEnd.authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type == "Boshliq":
                return HttpResponseRedirect(reverse("boshliq:admin_home"))
            elif user.user_type == "Sotuvchi":
                return HttpResponseRedirect(reverse("home_sotuvchi"))
                
        else:
            return HttpResponseRedirect("/")