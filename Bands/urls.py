from . import views
from django.urls import path

urlpatterns = [
    path('Musician/<int:musician_id>/', views.musician, name='musician'),
    path('All_Muscians/', views.allmusicians, name='Musicians'),
    path('Bands/', views.band_list, name='bands'),
    path('Bands_details/<int:band_id>/', views.band_detail, name='band'),
    path('Venues', views.venue_list, name='venues'),
]