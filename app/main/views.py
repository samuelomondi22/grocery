from django.shortcuts import render
from django.http import HttpResponse

# here we have an index page for our webapp
def index(response):
    return HttpResponse(
        #here's where we type our html
        "<h1>This is the grocery app</h1>"
        "<h2>Veiw 1</h2>"
        )