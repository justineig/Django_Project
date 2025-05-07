from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Musicians, Venue, Room, Band

def musician_detail(request, musician_id):
    musician = get_object_or_404(
        Musicians,
        pk=musician_id
    )
    return render(request, 'musician_details.html', {'musician': musician})

def all_musicians(request):
    musician_list = Musicians.objects.all().only('id', 'fullNames', 'telephone')
    paginator = Paginator(musician_list, 3)
    
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "all_musician.html", {'page_obj': page_obj})

def bands(request):
    bands = Band.objects.all().prefetch_related('musicians')
    return render(request, 'band_list.html', {'bands': bands})

def band(request, band_id):
    band = get_object_or_404(
        Band.objects.prefetch_related('musicians'),
        pk=band_id
    )
    return render(request, 'band_details.html', {'band': band})

def venue(request):
    venues = Venue.objects.prefetch_related('room_set')
    return render(request, 'venue_list.html', {'venues': venues})