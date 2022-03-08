from django.urls import path

from . import views

urlpatterns = [
    path("",views.crudhome,name="home"),
    path("save",views.save,name="save"),
    path("updatedel",views.updatedelete,name="updatedel"),
    path("deleteuser",views.deleteUser,name="deleteuser"),
    path("update",views.goupdate,name="update"),
    path("updateuser",views.updateuser,name="updateuser"),
    
]
