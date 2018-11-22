from django.urls import path

from . import views

urlpatterns = [
    path('', views.band_listing, name='band-list'),
    path('<int:band_id>/', views.band_detail, name='band-detail'),
    path('search/', views.band_search, name='band-search'),
]
