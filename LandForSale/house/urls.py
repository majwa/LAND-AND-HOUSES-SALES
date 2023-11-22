# house/urls.py

from django.urls import path
from .views import house_list, house_detail, house_search, house_home 

app_name = 'house'

urlpatterns = [
    path('list/', house_list, name='list'),
    path('<int:pk>/', house_detail, name='detail'),
    path('search/', house_search, name='search'),
    path('home/', house_home, name='home'),
    # Add other URLs as needed
]
