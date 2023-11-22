# land/urls.py
# land/urls.py

from django.urls import path
from .views import land_list, land_detail, land_search, land_home

app_name = 'land'

urlpatterns = [
    path('list/', land_list, name='list'),
    path('<int:pk>/', land_detail, name='detail'),
    path('search/', land_search, name='search'),
    
    # Add other URLs as needed
]
