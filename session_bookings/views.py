from django.shortcuts import render, get_object_or_404
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.views import generic, View
from .models import Booking

# Assitance from code institutes I think therefore I blog walkthrough tutorials


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'bookings.html'
    paginate_by = 6


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Booking.objects
        booking = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking
            },
        )
