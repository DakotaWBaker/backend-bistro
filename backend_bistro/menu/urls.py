from django.urls import path

from . import views

urlpatterns = [
    path("fullmenu", views.full_menu, name="full_menu"),
    path("csv", views.csv_view),
]
