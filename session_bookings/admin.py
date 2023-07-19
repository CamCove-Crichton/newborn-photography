from django.contrib import admin
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking, Todo
from django_summernote.admin import SummernoteModelAdmin


# Assitance from code institutes I think therefore I blog walkthrough tutorials
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('booking_name',)}
    list_filter = ('client', 'booking_date', 'status')
    list_display = ('booking_name', 'booking_date',
                    'slug', 'status', 'created_on')
    search_fields = ['booking_name', 'client',
                     'babys_name', 'special_requests']
    summernote_fields = ('special_requests')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status=1)


# Assitance from code institutes I think therefore I blog walkthrough tutorials
@admin.register(Todo)
class TodoAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'due_date', 'created_on')
    list_display = ('title', 'due_date', 'completed', 'created_on')
    search_fields = ['title', 'details']
    summernote_fields = ('details')
