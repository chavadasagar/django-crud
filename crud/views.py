from distutils.log import info
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import infos
# Create your views here.


def save(request):
    name = request.POST.get("name")
    age = request.POST.get("age")

    user = infos()
    user.name = name
    user.age = age

    user.save()


    return redirect("home")






def updatedelete(request):

    all = infos.objects.all()

    data = {
        "all":all
    }
    

    return render(request,"updatedel.html",data)

def delete(request):
    return HttpResponse("delete")


def goupdate(request):
    data = {

        "user":infos.objects.get(id=request.GET.get("id"))
    }

    return render(request,'update.html',data)
def crudhome(request):
    return render(request,'index.html')



def updateuser(request):

    pid = int(request.POST.get("id"))
    name = request.POST.get("name")
    age = request.POST.get("age")


    p = infos.objects.get(id=pid)
    p.name = name
    p.age = age


    p.save()

    return redirect("updatedel")

def deleteUser(request):
    uid = int(request.GET.get("id"))

    p = infos.objects.get(id=uid)

    p.delete()
    return redirect("updatedel")

