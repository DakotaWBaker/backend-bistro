from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fullmenu', views.full_menu, name = 'full_menu')
]