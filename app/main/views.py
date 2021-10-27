from os import name
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import groceries
from django.db.models import Q

# Create your views here.
def grocery_by_id(request, grocery_id):
    grocery = groceries.objects.get(pk=grocery_id)
    return render(request, 'grocery_details.html', {'grocery':grocery})

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = groceries
    template_name = 'search_results.html'

    def get_queryset(self):
        return groceries.objects.filter(Q(item__icontains=self.request.GET.get('q')))