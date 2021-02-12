from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
# Create your views here.

def index(respose,id):
	ls = ToDoList.objects.get(id=id)
	return render(respose,"main/list.html",{"ls":ls})

def home(respose):
	return render(respose,"main/home.html",{"name":"test"})