from django.db import models



class Tovar(models.Model):
    shtrix_code = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255)
    mahsulot_turi = models.CharField(max_length=255)
    mahsulot_hajmi = models.DecimalField(max_digits=9,default=0,decimal_places=2,blank=True,null=True)
    soni = models.PositiveIntegerField()
    umumiy_miqdori = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    kelgan_narxi = models.CharField(max_length=255)
    foizi = models.CharField(max_length=255)
    sotilish_narxi = models.CharField(max_length=255)
    firmasi = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

