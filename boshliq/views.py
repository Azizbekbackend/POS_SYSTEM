import re
from django.shortcuts import render,get_object_or_404,redirect
from accounts.models import Profile
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from .models import Tovar
import json
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage




def home(request):
    return render(request,'admin/home.html')


def xodim_page(request):
    profiles = Profile.objects.all()
    context = {
        "profiles":profiles
    }
    return render(request, 'admin/xodim_page.html', context)

def xodim_qoshish(request):
    if request.method!="POST":
        return HttpResponse("<h2>Xato Sorov</h2>")
    else:
        username=request.POST.get("username")
        password=request.POST.get("password")
        xodim_turi=request.POST.get("xodim_turi")
        try:
            user=Profile.objects.create_user(
                username=username,
                password=password,
                user_type=xodim_turi
            )
            user.save()
            messages.success(request,"Xodim Qoshildi")
            return HttpResponseRedirect(reverse("boshliq:xodim_page"))
        except:
            messages.error(request,"Xodim Qoshilmadi")
            return HttpResponseRedirect(reverse("boshliq:xodim_page"))


def xodim_delete(request,id):
    xodim = get_object_or_404(Profile, id=id)
    xodim.delete()
    messages.success(request, "Xodim O`chirib yuborildi!")
    return redirect(reverse('boshliq:xodim_page'))


def tovarlar_page(request):
    object_list = Tovar.objects.all()
    #pagination
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    q = request.GET.get('q')
    if q:
        tovarlar = object_list.filter(Q(name__contains=q))
    context = {
        "tovarlar":tovarlar
    }
    return render(request, 'admin/tovarlar.html',context)



def tovar_add_page(request):
    
    return render(request, 'admin/tovar_add_page.html')


def tovar_add_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Xato Sorov</h2>")
    else:
        # try:
        shtrix_code = request.POST.get('shtrix_kod')
        nomi = request.POST.get('nomi')
        mahsulot_type = request.POST.get("flexRadioDefault")
        if mahsulot_type == "Dona":
            tovar_tur = mahsulot_type
        elif mahsulot_type == "Kilogram":
            tovar_tur = mahsulot_type
        elif mahsulot_type == "Litr":
            tovar_tur = mahsulot_type
        mahsulot_hajmi = request.POST.get('mahuslot_hajmi')
        if mahsulot_hajmi == "":
            mahsulot_hajmi = None
        else:
            mahsulot_hajmi = mahsulot_hajmi
        soni = request.POST.get('soni')
        umumiy_miqdori = request.POST.get('umumiy_miqdori')
        kelgan_narxi = request.POST.get('kelgan_narxi')
        foizi = request.POST.get('foizi')
        sotilish_narxi = request.POST.get('sotilish_narxi')
        firmasi = request.POST.get('firma')
        try:
            tovar = Tovar.objects.get(shtrix_code=shtrix_code)
            tovar.shtrix_code = shtrix_code
            tovar.name = nomi
            tovar.mahsulot_turi = tovar_tur
            tovar.mahsulot_hajmi = mahsulot_hajmi
            tovar.soni += soni
            tovar.umumiy_miqdori = umumiy_miqdori
            tovar.kelgan_narxi = kelgan_narxi
            tovar.foizi = foizi
            tovar.sotilish_narxi = sotilish_narxi
            tovar.firmasi = firmasi
            tovar.save()
            messages.success(request,"Tovar Qo'shildi")
            return HttpResponseRedirect(reverse("boshliq:tovar_add_page"))
        except:
            tovar = Tovar.objects.create(
                shtrix_code=shtrix_code,
                name= nomi,
                mahsulot_turi=tovar_tur,
                mahsulot_hajmi=mahsulot_hajmi,
                soni=soni,
                umumiy_miqdori=umumiy_miqdori,
                kelgan_narxi=kelgan_narxi,
                foizi=foizi,
                sotilish_narxi=sotilish_narxi,
                firmasi=firmasi
            )
            tovar.save()
            messages.success(request,"Tovar Qo'shildi")
            return HttpResponseRedirect(reverse("boshliq:tovar_add_page"))
        # except:
        #     messages.error(request,"Tovar Qo'shilmadi")
        #     return HttpResponseRedirect(reverse("boshliq:tovar_add_page"))

def tovar_shtrix_code(request):
    if request.method!="POST":
        return HttpResponse("<h2>Xato Sorov</h2>")
    else:
        shtrix_code = request.POST.get('shtrix_code')
        data = []
        try:
            tovar = get_object_or_404(Tovar,shtrix_code=shtrix_code)
            tovar_obj = {}
            tovar_obj['nomi'] = tovar.name
            tovar_obj['mahsulot_turi'] = tovar.mahsulot_turi
            tovar_obj['mahsulot_hajmi'] = float(tovar.mahsulot_hajmi)
            tovar_obj['soni'] = tovar.soni
            tovar_obj['umumiy_miqdori'] = float(tovar.umumiy_miqdori)
            tovar_obj['kelgan_narxi'] = tovar.kelgan_narxi
            tovar_obj['foizi'] = tovar.foizi
            tovar_obj['sotilish_narxi'] = tovar.sotilish_narxi
            tovar_obj['firmasi'] = tovar.firmasi
            data.append(tovar_obj)
            return HttpResponse(json.dumps(data), content_type="application/json")
        except:
            return HttpResponse(json.dumps(data), content_type="application/json")

            
def tovar_tahrirlash(request,id):
    tovar = get_object_or_404(Tovar, id=id)
    context = {
        "tovar": tovar
    }
    return render(request, 'admin/tovar_update.html', context)


def tovar_tahrirlash_save(request):
    if request.method!= "POST":
        return HttpResponse("<h2>Xato Sorov</h2>")
    else:
        tovar_id = request.POST.get("tovar_id")
        shtrix_code = request.POST.get('shtrix_kod')
        nomi = request.POST.get('nomi')
        mahsulot_type = request.POST.get("flexRadioDefault")
        if mahsulot_type == "Dona":
            tovar_tur = mahsulot_type
        elif mahsulot_type == "Kilogram":
            tovar_tur = mahsulot_type
        elif mahsulot_type == "Litr":
            tovar_tur = mahsulot_type
        mahsulot_hajmi = request.POST.get('mahuslot_hajmi')
        if mahsulot_hajmi == "":
            mahsulot_hajmi = None
        else:
            mahsulot_hajmi = mahsulot_hajmi
        soni = request.POST.get('soni')
        umumiy_miqdori = request.POST.get('umumiy_miqdori')
        kelgan_narxi = request.POST.get('kelgan_narxi')
        foizi = request.POST.get('foizi')
        sotilish_narxi = request.POST.get('sotilish_narxi')
        firmasi = request.POST.get('firma')
        try:
            tovar = Tovar.objects.get(id=tovar_id)
            tovar.shtrix_code = shtrix_code
            tovar.name = nomi
            tovar.mahsulot_turi = tovar_tur
            tovar.mahsulot_hajmi = mahsulot_hajmi
            tovar.soni = soni
            tovar.umumiy_miqdori = umumiy_miqdori
            tovar.kelgan_narxi = kelgan_narxi
            tovar.foizi = foizi
            tovar.sotilish_narxi = sotilish_narxi
            tovar.firmasi = firmasi
            tovar.save()
            messages.success(request,"Tovar Tahrirlandi")
            return HttpResponseRedirect(reverse("boshliq:tovar_tahrirlash",kwargs={"id":tovar_id}))
        except:
            messages.error(request,"Tovar Tahrirlanmadi")
            return HttpResponseRedirect(reverse("boshliq:tovar_tahrirlash",kwargs={"id":tovar_id}))
