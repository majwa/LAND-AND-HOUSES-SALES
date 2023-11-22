# land/views.py

from django.shortcuts import render, get_object_or_404
from .models import Land
from .forms import LandSearchForm

def land_list(request):
    lands = Land.objects.all()
    return render(request, 'land/land_list.html', {'lands': lands})

def land_detail(request, pk):
    land = get_object_or_404(Land, pk=pk)
    return render(request, 'land/land_detail.html', {'land': land})

def land_list(request):
    lands = Land.objects.all()
    return render(request, 'land/land_list.html', {'lands': lands})

def land_home(request):
    latest_lands = Land.objects.order_by('-created_at')[:3]
    return render(request, 'home.html', {'latest_lands': latest_lands})

def land_search(request):
    form = LandSearchForm(request.GET)

    if form.is_valid():
        location = form.cleaned_data.get('location', '')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        lands = Land.objects.filter(location__icontains=location)

        if min_price:
            lands = lands.filter(price__gte=min_price)

        if max_price:
            lands = lands.filter(price__lte=max_price)

    else:
        lands = Land.objects.all()

    return render(request, 'land/land_list.html', {'lands': lands, 'form': form})