from django.urls import path

from . import views

urlpatterns = [
# path for our index page, the first parameter is where the path of the page
path("", views.index, name="index"),
]