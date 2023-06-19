# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.shortcuts import render, get_object_or_404
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.views import generic, View
from .models import Booking
from .forms import BookingForm

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


class Home(View):
    def get(self, request):
        return render(request, "index.html")


# class NewBooking(generic.ListView):
#     model = Booking
#     template_name = 'new_booking.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = BookingForm()
#         return context

#     def post(self, request, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = BookingForm()

#         new_booking_request = BookingForm(data=request.POST)

#         if new_booking_request.is_valid():
#             new_booking_request.instance.email = request.user.email
#             new_booking_request.instance.name = request.user.username
#         else:
#             new_booking_request = BookingForm()

#         return context

class NewBooking(generic.ListView):
    model = Booking

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "new_booking.html",
            {
                "submitted": False,
                "form": BookingForm()
            },
        )

    def post(self, request, *args, **kwargs):

        new_booking_request = BookingForm(data=request.POST)

        if new_booking_request.is_valid():
            new_booking_request.instance.email = request.user.email
            new_booking_request.instance.name = request.user.username
        else:
            new_booking_request = BookingForm()

        return render(
            request,
            "new_booking.html",
            {
                "submitted": True,
                "form": BookingForm()
            },
        )
