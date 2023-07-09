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
from django.contrib import messages

from datetime import datetime
from .utils.booking_utils import validate_booking_date


# Assitance from code institutes I think therefore I blog walkthrough
# tutorials & ChatGpt
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
        queryset = super().get_queryset().filter(client=user).order_by(
            '-booking_date')

        return queryset


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingDetail(View):
    """
    BookingDetail class gets all the details about a booking to display it to
    the user
    """

    def get(self, request, slug, *args, **kwargs):
        # Assistance from ChatGpt
        booking = get_object_or_404(Booking, slug=slug)
        todos = Todo.objects.filter(booking_id=booking)

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking,
                "todos": todos
            },
        )


class Home(View):
    """
    The Home class returns the render of the index.html file to return to the
    home page
    """

    def get(self, request):
        return render(request, "index.html")


class NewBooking(LoginRequiredMixin, generic.ListView):
    """
    The NewBooking class is to create a view for users to fill in a form and
    submit it to make a booking
    """
    model = Booking
    form_class = BookingForm

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials
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

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials
    def post(self, request, *args, **kwargs):
        """
        Submits the new booking request, when it is valid, to the database
        """
        new_booking_request = BookingForm(request.POST, request.FILES)

        # Assitance from code institutes I think therefore I blog walkthrough
        # tutorials & ChatGpt
        if new_booking_request.is_valid():
            # Validate booking date is not before due date
            booking_date = new_booking_request.cleaned_data['booking_date']
            due_date = new_booking_request.cleaned_data['babys_due_date']
            if not validate_booking_date(self, booking_date, due_date):
                messages.error(
                    request, "Invalid date. Booking date cannot be before the due date.")
                return render(
                    request,
                    "new_booking.html",
                    {
                        "form": BookingForm()
                    },
                )

            # Check for existing booking in database
            existing_booking = Booking.objects.filter(
                booking_date=booking_date).first()
            if existing_booking:
                messages.error(
                    request, "The selected date is unavailable, please choose a different date.")
                return render(
                    request,
                    "new_booking.html",
                    {
                        "form": BookingForm()
                    },
                )
            else:
                booking = new_booking_request.save(commit=False)
                booking.client = request.user
                booking.slug = slugify(booking.booking_name)
                booking.featured_image = new_booking_request.cleaned_data[
                    'featured_image']
                booking.status = 1
                booking.save()

                # Display success message
                messages.success(
                    request, "Session booking successfully requested")
                return redirect('bookings')
        else:
            # Display error message
            messages.error(
                request, "Invalid form data, please check your inputs")
            return render(
                request,
                "new_booking.html",
                {
                    "form": BookingForm()
                },
            )


class EditBooking(LoginRequiredMixin, generic.ListView):
    """
    The EditBooking class is to create a view for users to be able to edit
    their booking details
    """
    model = Booking

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials
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

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials
    def post(self, request, *args, **kwargs):
        """
        Submits the updated booking request, when it is valid, to the database
        """
        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(request.POST, request.FILES, instance=booking)
        context = {
            "form": form
        }

        unedited_date = booking.booking_date

        # Assitance from code institutes I think therefore I blog walkthrough
        # tutorials & ChatGpt
        if form.is_valid():
            edited_booking = form.save(commit=False)
            # Check if the booking date has been modifed
            if edited_booking.booking_date != unedited_date:
                # Perform duplicate data check
                duplicate_booking = Booking.objects.filter(
                    booking_date=edited_booking.booking_date).exclude(
                        id=booking_id).first()
                if duplicate_booking:
                    # Display error message
                    messages.error(
                        request, "The selected date is unavailable, please choose a different date.")
                    return render(request, "edit_booking.html", context)

            # Validate booking date is not before due date
            booking_date = edited_booking.booking_date
            due_date = edited_booking.babys_due_date
            if not validate_booking_date(self, booking_date, due_date):
                # Display error message
                messages.error(
                    request, "Invalid date. Booking date cannot be before the due date.")
                return render(request, "edit_booking.html", context)

            edited_booking.client = request.user
            edited_booking.slug = slugify(edited_booking.booking_name)
            edited_booking.featured_image = form.cleaned_data[
                'featured_image']
            edited_booking.status = 1
            edited_booking.save()
            # Display success message
            messages.success(request, "Session booking successfully updated")
            return redirect('bookings')
        else:
            # Display error message
            messages.error(
                request, "Invalid form data, please check your inputs")
            return render(request, "edit_booking.html", context)


# Assistance from Code Institutes Hello Django & I think therefore I blog
# walkthrough tutorials
class DeleteBooking(LoginRequiredMixin, generic.ListView):
    """
    The DeleteBooking class is to enable users to delete one of thier bookings
    """
    model = Booking

    def get(self, request, *args, **kwargs):
        """
        Fetches the content to delete a record from the database which uses
        the booking id
        """
        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)

        booking.delete()
        # Display success message
        messages.success(request, "Session booking successfully deleted")

        return redirect('bookings')


# Assitance from Code Institutes I thing therefore I blog walkthrough
# tutorials and ChatGpt
@method_decorator(
    staff_member_required(login_url='account_login'), name='dispatch')
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

            todo_item.save()
            # Display success message
            messages.success(request, "New Todo item successfully added")

            return redirect('booking_detail', slug=booking_slug, id=booking_id)
        else:
            # Display error message
            messages.error(
                request, "Invalid form data, please check your inputs")
            return render(
                request,
                "new_todo.html",
                {
                    "form": form
                },
            )


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class TodoDetail(View):
    """
    TodoDetail class gets all the details about a todo item to display it to
    the admin
    """

    def get(self, request, slug, id):
        # Assistance from ChatGpt
        todo_item = get_object_or_404(Todo, slug=slug, id=id)

        return render(
            request,
            "todo_detail.html",
            {
                "todo_item": todo_item
            },
        )


class EditTodo(LoginRequiredMixin, generic.ListView):
    """
    The EditTodo class is to create a view for the admin to be able to edit
    their todo items details
    """
    model = Todo

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials & from ChatGpt
    def get(self, request, *args, **kwargs):
        """
        Fetches the content to display from the TodoForm() which uses
        crispy forms and is located in the forms.py file
        """
        todo_id = kwargs['id']
        todo_item = get_object_or_404(Todo, id=todo_id)
        booking = todo_item.booking_id

        form = TodoForm(instance=todo_item)
        context = {
            "form": form,
            "booking_slug": booking.slug,
            "booking_id": booking.id
        }

        return render(request, "edit_todo.html", context)

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials & from ChatGpt
    def post(self, request, *args, **kwargs):
        """
        Submits the updated Todo request, when it is valid, to the database
        """

        todo_id = kwargs['id']
        todo_item = get_object_or_404(Todo, id=todo_id)
        form = TodoForm(instance=todo_item)
        context = {
            "form": form
        }

        update_todo = TodoForm(
            request.POST, instance=todo_item)

        # Assitance from code institutes I think therefore I blog walkthrough
        # tutorials & ChatGpt
        if update_todo.is_valid():
            todo_item = update_todo.save(commit=False)
            todo_item.slug = slugify(todo_item.title)
            todo_item.save()

            # Get the booking related to the todo item
            booking_slug = todo_item.booking_id.slug
            booking_id = todo_item.booking_id.id

            # Display success message
            messages.success(request, "Todo item successfully updated")

            return redirect('booking_detail', slug=booking_slug, id=booking_id)
        else:
            # Display error message
            messages.error(
                request, "Invalid form data, please check your inputs")
            return render(request, "edit_todo.html", context)


# Assistance from Code Institutes Hello Django & I think therefore I blog
# walkthrough tutorials
class DeleteTodo(LoginRequiredMixin, generic.ListView):
    """
    The DeleteTodo class is to enable the admin to delete one of thier
    todo items
    """
    model = Todo

    def get(self, request, *args, **kwargs):
        """
        Fetches the content to delete a record from the database which uses
        the booking id
        """
        todo_id = kwargs['id']
        todo_item = get_object_or_404(Todo, id=todo_id)

        # Get the booking related to the todo item
        booking_slug = todo_item.booking_id.slug
        booking_id = todo_item.booking_id.id

        todo_item.delete()

        # Display success message
        messages.success(request, "Todo item successfully deleted")

        return redirect('booking_detail', slug=booking_slug, id=booking_id)
