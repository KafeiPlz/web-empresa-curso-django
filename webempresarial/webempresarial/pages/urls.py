from django.urls import path
from . import views

urlpatterns = [
#path de core
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page") #category_id siempre es cadena de caracteres, int lo transforma en entero
]
