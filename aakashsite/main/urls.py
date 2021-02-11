from django.urls import path

from . import views

urlpatterns = [
path("",views.index,name="index"), # once admin routes to this url pattern it will call the views.index
path("greet/",views.index1,name="")
]