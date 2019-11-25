from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models


class ReservationDetail(DetailView):

    """ ReservationDetail Definition"""

    reservation = models.Reservation


class SearchView(View):

    """ SearchView Definition"""

    def get(self, request):
        return render(request, "reservations/reservation_detail.html")
