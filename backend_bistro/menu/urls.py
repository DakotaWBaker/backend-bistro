from django.urls import path

from . import views

urlpatterns = [
    path('fullmenu', views.full_menu, name = 'full_menu'),
    path('ctv', views.ctv_view)
]