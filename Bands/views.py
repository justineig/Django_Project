from django.shortcuts import get_object_or_404, render
from Bands.models import Musicians,Venue,Room,Band
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def musician(request, musician_id):
    musician = get_object_or_404(Musicians, id=musician_id)
    return render(request, 'Muscian.html', {'musician': musician})

def allmusicians(request):
    musician_list = Musicians.objects.all().order_by('fullNames')
    paginator = Paginator(musician_list, 3) 
    
    page = request.GET.get('page')
    try:
        musicians = paginator.page(page)
    except PageNotAnInteger:
        musicians = paginator.page(1)
    except EmptyPage:
        musicians = paginator.page(paginator.num_pages)
    
    return render(request, "allmusicians.html", {'musicians': musicians, 'page': musicians})

def band_list(request):
    bands= Band.objects.all()
    return render(request, 'bands.html', {'bands':bands})

def band_detail(request, band_id):
    band = Band.objects.get(pk=band_id)
    return render(request, 'band_details.html', {'band': band})

def venue_list(request):
    venues = Venue.objects.prefetch_related('room_set')
    return render(request, 'venues.html', {'venues': venues})