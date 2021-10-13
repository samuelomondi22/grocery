from os import name
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import groceries
from django.db.models import Q

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def book_by_id(request, book_id):
    book = groceries.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = groceries
    template_name = 'search_results.html'

    def get_queryset(self):
        return groceries.objects.filter(Q(title__icontains=' ') | 
        Q(pub_date__icontains='12:52')
        )