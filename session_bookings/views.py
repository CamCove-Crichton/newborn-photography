# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Booking, Todo
from .forms import BookingForm, TodoForm

# Assistance from ChatGpt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


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


# Assistance from Code Institutes Hello Django & I think therefore I blog walkthrough tutorials
class DeleteBooking(LoginRequiredMixin, generic.ListView):
    """
    The DeleteBooking class is to enable users to delete one of thier bookings
    """
    model = Booking

    def get(self, request, *args, **kwargs):
        """
        Fetches the content to delete a record from the database which uses the booking id
        """
        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
        context = {
            "form": form
        }

        booking.delete()

        return redirect('bookings')


# Assitance from Code Institutes I thing therefore I blog walkthrough tutorials and ChatGpt
@method_decorator(staff_member_required(login_url='account_login'), name='dispatch')
class AdministratorView(generic.ListView):

    model = Booking
    template_name = 'administrator_panel.html'
    paginate_by = 6
    context_object_name = 'bookings'

    def get_queryset(self):
        return super().get_queryset().order_by('booking_date')


class NewTodo(LoginRequiredMixin, generic.ListView):
    """
    The NewTodo class is to create a view for superusers to fill in a todo form
    and submit it to add to a list of todo items related to that booking
    """
    model = Todo
    form_class = TodoForm

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials & ChatGpt
    def get(self, request, *args, **kwargs):
        """
        Fetches the content to display from the TodoForm() which uses
        crispy forms and is located in the forms.py file
        """

        # Get the slug and id from the URL parameters
        slug = self.kwargs['slug']
        booking_id = self.kwargs['id']

        # Retrieve the booking object based on the slug and id
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, slug=slug, id=booking_id)

        return render(
            request,
            "new_todo.html",
            {
                "form": TodoForm(),
                "booking": booking,
            },
        )

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials & ChatGpt

    def post(self, request, *args, **kwargs):
        """
        Submits the new todo item, when it is valid, to the database
        """

        form = TodoForm(request.POST)

        print("Before if statement")
        if form.is_valid():
            todo_item = form.save(commit=False)

            # Get the booking related to the todo item
            booking_slug = request.POST['slug']
            booking_id = request.POST['id']
            booking = get_object_or_404(
                Booking, slug=booking_slug, id=booking_id)

            # Set the booking_id and slug for the todo item
            todo_item.booking_id = booking
            todo_item.slug = slugify(todo_item.title)
            print(booking_id)

            todo_item.save()

            return redirect('booking_detail', slug=booking_slug, id=booking_id)
        else:
            return render(
                request,
                "new_todo.html",
                {
                    "form": form
                },
            )
