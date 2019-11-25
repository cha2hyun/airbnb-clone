from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("<int:pk>", views.ReservationDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
