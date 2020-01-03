import datetime
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from . import models


class CreateError(Exception):
    pass


def create(request, room, year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't Reserve that room")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj+datetime.timedelta(days=1)
        )
        return redirect(reverse("reservation:detail", kwargs={"pk": reservation.pk}))


class ReservationDetail(View):

    """ ReservationDetail Definition"""

    def get(self, pk):
        reservation = models.Reservation.objects.get_or_none(pk=pk)
        if not reservation:
            return redirect(reverse("core:home"))


class SearchView(View):

    """ SearchView Definition"""

    def get(self, request):
        return render(request, "reservations/reservation_detail.html")
