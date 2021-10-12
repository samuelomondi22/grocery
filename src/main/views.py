from django.shortcuts import render
from django.http import HttpResponse

# here we have an index page for our webapp
def index(response):
    return HttpResponse(
        #here's where we type our html
        "<h1>This is the index page</h1>"
        "<h1>Veiw 1</h1>"
        )