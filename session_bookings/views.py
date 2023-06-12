from django.shortcuts import render
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.views import generic
from .models import Booking

class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'bookings.html'
    paginate_by = 6
