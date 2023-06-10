from django.contrib import admin
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


# Assitance from code institutes I think therefore I blog walkthrough tutorials
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('booking_name',)}
    list_filter = ('client', 'booking_date', 'status')
    list_display = ('booking_name', 'booking_date', 'slug', 'status', 'created_on')
    search_fields = ['booking_name', 'client',
                     'babys_name', 'special_requests']
    summernote_fields = ('special_requests')
