from django.urls import path
from .views import home_sotuvchi

urlpatterns = [
    path('home/',home_sotuvchi, name="home_sotuvchi"),
]