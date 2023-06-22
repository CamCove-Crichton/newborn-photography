# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking
from django.contrib.auth.models import User
from django import forms


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingForm(forms.ModelForm):
    """
    The New Booking Request form which utilises crispy forms in
    the html template
    """
    class Meta:
        model = Booking
        fields = ('booking_name', 'booking_date', 'booking_time',
                  'babys_due_date', 'babys_name', 'babys_gender',
                  'location', 'special_requests', 'how_you_found_me',
                  'consent', 'featured_image',)
