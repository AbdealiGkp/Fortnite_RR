from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='hello'),
    path('rick', views.rrpage, name='rickroll'),
]