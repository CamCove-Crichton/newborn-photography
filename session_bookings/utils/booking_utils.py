# Idea of creating new booking_utils.py from ChatGpt
from datetime import datetime
from django.contrib import messages


def validate_booking_date(self, date1, date2):
    """
    Validates the booking date is not before the due date when
    a booking is requested
    """
    try:
        formats = ['%d-%m-%y', '%d-%m-%Y']
        for fmt in formats:
            booking_datetime = datetime.combine(date1, datetime.min.time())
            due_datetime = datetime.combine(date2, datetime.min.time())
            booking_date = booking_datetime.strftime(fmt)
            due_date = due_datetime.strftime(fmt)
            booking_datetime = datetime.strptime(booking_date, fmt)
            due_datetime = datetime.strptime(due_date, fmt)
            if booking_datetime > due_datetime:
                return True
    except ValueError:
        return False


def handle_form_validation_errors(request, form):
    """
    A function to handle any errors thrown when a form is validated and returns
    errors, but will display in a human readable format using djamgo messages
    """
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(
                request, f"Invalid input in the {field} field. {error}")
