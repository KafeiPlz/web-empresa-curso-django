from django.urls import path
from . import views

urlpatterns = [
#path de core
    path('', views.blog, name ='blog'),
    path('category/<int:category_id>/', views.category, name="category") #category_id siempre es cadena de caracteres, int lo transforma en entero
]
