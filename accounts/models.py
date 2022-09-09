from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Profile(AbstractUser):
    user_type_data=(
        ("Boshliq","Boshliq"),
        ("Sotuvchi","Sotuvchi"),
    )
    user_type=models.CharField(default="Boshliq",choices=user_type_data,max_length=50,verbose_name="Xodim Turi")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user_type}"