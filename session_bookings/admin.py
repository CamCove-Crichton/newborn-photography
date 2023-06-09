from django.contrib import admin
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('special_requests')

# Assitance from code institutes I think therefore I blog walkthrough tutorials
admin.site.register(Booking)
