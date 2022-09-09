from django.shortcuts import render




def home_sotuvchi(request):
    return render(request,'sotuvchi/home.html')
