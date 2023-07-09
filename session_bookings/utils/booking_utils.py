# Idea of creating new booking_utils.py from ChatGpt
from datetime import datetime


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
