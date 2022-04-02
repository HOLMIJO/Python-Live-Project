from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_home, name='weather_home'),
    path('weathercreate/', views.weather_create, name='weather_create'),
    path('weatherdisplaydb/', views.weather_db, name='weather_db'),
    path('<int:pk>/weatherdetails/', views.weather_details, name='weather_details'),
    path('<int:pk>/weatheredit/', views.weather_edit, name='weather_edit'),
    path('<int:pk>/weatherdelete/', views.weather_delete, name='weather_delete'),
    path('weatherscraping/', views.weather_scraping, name='weather_scraping'),
    path('weatherapi/', views.weather_api, name='weather_api'),
]