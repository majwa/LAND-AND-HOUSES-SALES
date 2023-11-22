# house/views.py

from django.shortcuts import render, get_object_or_404
from .models import House
from .forms import HouseSearchForm

def house_list(request):
    houses = House.objects.all()
    return render(request, 'house/house_list.html', {'houses': houses})

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'house/house_detail.html', {'house': house})

def house_home(request):
    latest_houses = House.objects.order_by('-created_at')[:3]
    return render(request, 'home.html', {'latest_houses': latest_houses})

def house_search(request):
    form = HouseSearchForm(request.GET)

    if form.is_valid():
        location = form.cleaned_data.get('location', '')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        houses = House.objects.filter(location__icontains=location)

        if min_price:
            houses = houses.filter(price__gte=min_price)

        if max_price:
            houses = houses.filter(price__lte=max_price)

    else:
        houses = House.objects.all()

    return render(request, 'house/house_list.html', {'houses': houses, 'form': form})