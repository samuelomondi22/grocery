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
    item = request.GET.get('q')
    
    # This will update or add grocerys if you want
    if request.method == "POST":
        new_walmart_price = request.POST.get('walmart_price')
        new_broulims_price = request.POST.get('broulims_price')
        new_albertsons_price = request.POST.get('albertsons_price')

        # if request.POST.get('owned') is None:
        #     new_owned = False
        # else:
        #     new_owned = request.POST.get('owned')
        
        # if Stock.objects.filter(ticker=new_ticker).exists():
        #     Stock.objects.filter(ticker=new_ticker).update(ask=new_ask)
        #     Stock.objects.filter(ticker=new_ticker).update(bid=new_bid)
        #     Stock.objects.filter(ticker=new_ticker).update(owned=new_owned)
        # else:
        #     s = Stock(ticker=new_ticker, ask=new_ask, bid=new_bid, owned=new_owned)
        #     s.save()

    context = {
        'item':item
    }
    return render(request, "add_grocery.html", context)

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = groceries
    template_name = 'search_results.html'

    def get_queryset(self):
        return groceries.objects.filter(Q(item__icontains=self.request.GET.get('q')))