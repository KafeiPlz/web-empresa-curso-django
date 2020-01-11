from django.urls import path
from . import views

urlpatterns = [
#path de core
    path('', views.contact, name ='contact'),
]
