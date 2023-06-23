# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.shortcuts import render, get_object_or_404, redirect
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.views import generic, View
from .models import Booking
from .forms import BookingForm
# Assistance from ChatGpt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify


# Assitance from code institutes I think therefore I blog walkthrough tutorials & ChatGpt
class BookingList(LoginRequiredMixin, generic.ListView):
    """
    BookingList class creates a view for the user to see all the bookings made
    """
    model = Booking
    template_name = 'bookings.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Filters bookings to display only the currently logged in users bookings
        """
        # Assitance from ChatGpt
        user = self.request.user
        queryset = super().get_queryset().filter(client=user).order_by('-booking_date')

        return queryset


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingDetail(View):
    """
    BookingDetail class gets all the details about a booking to display it to the user
    """

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
    """
    The Home class returns the render of the index.html file to return to the home page
    """

    def get(self, request):
        return render(request, "index.html")


class NewBooking(LoginRequiredMixin, generic.ListView):
    """
    The NewBooking class is to create a view for users to fill in a form and submit it to make a booking
    """
    model = Booking
    form_class = BookingForm

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def get(self, request, *args, **kwargs):
        """
        Fetches the content to display from the BookingForm() which uses
        crispy forms and is located in the forms.py file
        """

        return render(
            request,
            "new_booking.html",
            {
                "form": BookingForm()
            },
        )

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def post(self, request, *args, **kwargs):
        """
        Submits the new booking request, when it is valid, to the database
        """

        new_booking_request = BookingForm(request.POST, request.FILES)

        # Assitance from code institutes I think therefore I blog walkthrough tutorials & ChatGpt
        if new_booking_request.is_valid():
            booking = new_booking_request.save(commit=False)
            booking.client = request.user
            booking.slug = slugify(booking.booking_name)
            booking.featured_image = new_booking_request.cleaned_data['featured_image']
            booking.save()
            return redirect('bookings')
        else:
            return render(
                request,
                "new_booking.html",
                {
                    "form": BookingForm()
                },
            )


class EditBooking(LoginRequiredMixin, generic.ListView):
    """
    The EditBooking class is to create a view for users to be able to edit their booking details
    """
    model = Booking

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def get(self, request, *args, **kwargs):
        """
        Fetches the content to display from the BookingForm() which uses
        crispy forms and is located in the forms.py file
        """
        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
        context = {
            "form": form
        }

        return render(request, "edit_booking.html", context)

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def post(self, request, *args, **kwargs):
        """
        Submits the new booking request, when it is valid, to the database
        """

        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
        context = {
            "form": form
        }

        update_booking = BookingForm(
            request.POST, request.FILES, instance=booking)

        # Assitance from code institutes I think therefore I blog walkthrough tutorials & ChatGpt
        if update_booking.is_valid():
            booking = update_booking.save(commit=False)
            booking.client = request.user
            booking.slug = slugify(booking.booking_name)
            booking.featured_image = update_booking.cleaned_data['featured_image']
            booking.save()
            return redirect('bookings')
        else:
            return render(request, "edit_booking.html", context)
