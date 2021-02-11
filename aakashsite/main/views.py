from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(respose):
	return HttpResponse("<h1>Aakash is awesome</h1>")

def index1(respose):
	return HttpResponse("<h1>Greetings from Aakash</h1>")