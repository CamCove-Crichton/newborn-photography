from django.contrib import admin
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking, Todo
from django_summernote.admin import SummernoteModelAdmin


# Assitance from code institutes I think therefore I blog walkthrough tutorials
class BookingAdmin(SummernoteModelAdmin):

    summernote_fields = ('special_requests')


# Assitance from code institutes I think therefore I blog walkthrough tutorials
@admin.register(Todo)
class TodoAdmin(SummernoteModelAdmin):

    list_filter = ('title', 'due_date', 'created_on')
    list_display = ('title', 'due_date', 'completed', 'created_on')
    search_fields = ['title', 'details']
    summernote_fields = ('details')
