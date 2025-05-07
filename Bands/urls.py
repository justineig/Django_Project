from . import views
from django.urls import path

urlpatterns = [
    path('musicians/', views.all_musicians, name='all_musicians'),
    path('musicians/<int:musician_id>/', views.musician_detail, name='musician_detail'),
    
    path('bands/', views.bands, name='band_list'),
    path('bands/<int:band_id>/', views.band, name='band_detail'),
    
    path('venues/', views.venue, name='venue_list'),
]