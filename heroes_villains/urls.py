from django.urls import path
from . import views

urlpatterns = [
    path('', views.heroes_villains_list),
]