from django.urls import path
from .views import home, xodim_page,xodim_delete,xodim_qoshish,tovarlar_page,tovar_add_page,tovar_add_save,tovar_shtrix_code,tovar_tahrirlash,tovar_tahrirlash_save,tovar_delete
app_name = 'boshliq'

urlpatterns = [
    path('home/',home,name="admin_home"),
    path('xodimlar-boshqaruv/', xodim_page, name="xodim_page"),
    path('xodim-ochirish/<int:id>',xodim_delete, name="xodim_delete"),
    path('xodim_qoshish',xodim_qoshish, name="xodim_qoshish"),
    path('tovarlar/',tovarlar_page,name="tovarlar_page"),
    path('tovar-qoshish/',tovar_add_page,name="tovar_add_page"),
    path('tovar_add_save',tovar_add_save,name="tovar_add_save"),
    path('tovar_shtrix_code',tovar_shtrix_code,name="tovar_shtrix_code"),
    path('tovar_tahrirlash/<int:id>',tovar_tahrirlash,name="tovar_tahrirlash"),
    path('tovar_tahrirlash_save',tovar_tahrirlash_save,name="tovar_tahrirlash_save"),
    path('tovar_delete/<int:id>',tovar_delete, name="tovar_delete"),

]