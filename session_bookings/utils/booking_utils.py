# Idea of creating new booking_utils.py from ChatGpt
from datetime import datetime, date
from django.contrib import messages


# Assitance from Chatgpt
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


# Assitance from Chatgpt
def handle_form_validation_errors(request, form):
    """
    A function to handle any errors thrown when a form is validated and returns
    errors, but will display in a human readable format using djamgo messages
    """
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(
                request, f"Invalid input in the {field} field. {error}")


# Assitance from Chatgpt
def booking_date_vs_todays_date(datedata):
    """
    A function to handle the validation of the booking date not being before
    today's date
    """
    formats = ['%d-%m-%y', '%d-%m-%Y']

    # Convert the date object to a string using strftime()
    datedata_str = datedata.strftime('%d-%m-%y')

    for fmt in formats:
        try:
            booking_date = datetime.strptime(datedata_str, fmt)
            today = date.today()

            if booking_date.date() > today:
                return True
            else:
                return False
        except ValueError:
            pass

    return False


def validate_booking_time(timedata):
    """
    A function to validate the booking time requested falls between 9am and 3pm
    """
    # Convert booking time input to a string
    timedata_str = timedata.strftime('%H:%M')

    try:
        # Convert the string to a time object
        time_object = datetime.strptime(timedata_str, '%H:%M').time()

        # Set start and end times to check against
        start_time = datetime.strptime('09:00', '%H:%M').time()
        end_time = datetime.strptime('15:00', '%H:%M').time()

        # Check if booking falls in the specified time range
        if start_time <= time_object <= end_time:
            return True
        else:
            return False
    except ValueError:
        return False
