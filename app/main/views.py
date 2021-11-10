from os import name
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import groceries
from django.db.models import Q

# Create your views here.
def grocery_by_id(request, grocery_id):
    grocery = groceries.objects.get(pk=grocery_id)
    return render(request, 'grocery_details.html', {'grocery':grocery})

def add_grocery(request):
    new_item = request.GET.get('q')
    
    # This will update or add grocerys if you want
    if request.method == "POST":
        new_walmart_price = request.POST.get('walmart_price')
        new_broulims_price = request.POST.get('broulims_price')
        new_albertsons_price = request.POST.get('albertsons_price')
        
        grocery = groceries.objects.filter(item=new_item)

        if grocery.exists():
            grocery.update(walmart_price=new_walmart_price)
            grocery.update(broulims_price=new_broulims_price)
            grocery.update(albertsons_price=new_albertsons_price)
        else:
            s = groceries(item=new_item, walmart_price=new_walmart_price, broulims_price=new_broulims_price, albertsons_price=new_albertsons_price)
            s.save()

    context = {
        'item':new_item
    }
    return render(request, "add_grocery.html", context)

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = groceries
    template_name = 'search_results.html'

    def get_queryset(self):
        return groceries.objects.filter(Q(item__icontains=self.request.GET.get('q')))