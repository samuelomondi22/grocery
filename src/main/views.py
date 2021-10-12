from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>This is the index page</h1>")

def v1(response):
    return HttpResponse("<h1>Veiw 1</h1>")