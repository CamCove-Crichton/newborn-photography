# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.shortcuts import render, get_object_or_404
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
# Assistance from ChatGpt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.text import slugify


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


class NewBooking(LoginRequiredMixin, generic.ListView):
    model = Booking
    form_class = BookingForm

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "new_booking.html",
            {
                "submitted": False,
                "form": BookingForm()
            },
        )

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def post(self, request, *args, **kwargs):

        new_booking_request = BookingForm(request.POST, request.FILES)

        # Assitance from code institutes I think therefore I blog walkthrough tutorials & ChatGpt
        if new_booking_request.is_valid():
            booking = new_booking_request.save(commit=False)
            booking.client = request.user
            booking.slug = slugify(booking.booking_name)
            booking.featured_image = new_booking_request.cleaned_data['featured_image']
            booking.save()
            return render(request, "bookings.html")
        else:
            return render(
                request,
                "new_booking.html",
                {
                    "submitted": True,
                    "form": BookingForm()
                },
            )
