from django.urls import path

from . import views

urlpatterns = [
path("<int:id>",views.index,name="index"), # once admin routes to this url pattern it will call the views.index
path("",views.home,name="home")
]