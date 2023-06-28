# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking, Todo
from django.contrib.auth.models import User
from django import forms


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingForm(forms.ModelForm):
    """
    The New Booking Request form which utilises crispy forms in
    the html template
    """
    # Assitance from ChatGpt on how to change the accepted date format input in the form
    booking_date = forms.DateField(
        input_formats=['%d-%m-%y', '%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%y'),)
    babys_due_date = forms.DateField(
        input_formats=['%d-%m-%y', '%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%y'),)
    booking_time = forms.TimeField(
        input_formats=['%H:%M'], widget=forms.TimeInput(format='%H:%M'),)

    class Meta:
        model = Booking
        fields = ('booking_name', 'booking_date', 'booking_time',
                  'babys_due_date', 'babys_name', 'babys_gender',
                  'location', 'special_requests', 'how_you_found_me',
                  'consent', 'featured_image',)


class TodoForm(forms.ModelForm):
    """
    The Todo form allows the admin to fill in details about the Todo item,
    utilising crispy forms in the html template
    """
    due_date = forms.DateField(
        input_formats=['%d-%m-%y', '%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%y'),)
    due_time = forms.TimeField(
        input_formats=['%H:%M'], widget=forms.TimeInput(format='%H:%M'),)

    class Meta:
        model = Todo
        fields = ('title', 'details', 'due_date', 'due_time', 'completed',)
