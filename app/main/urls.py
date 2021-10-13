from django.urls import path
from .backend import CrudAPIView
from . import views
from .views import HomePageView, SearchResultsView

urlpatterns = [
# path for our index page, the first parameter is where the path of the page
    # path("", views.index, name="index"),
    path('crud', CrudAPIView.as_view()),
    path('crud/<str:pk>', CrudAPIView.as_view()),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home')
]
