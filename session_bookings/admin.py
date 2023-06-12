from django.contrib import admin
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from .models import Booking, Todo, PersonalInfo
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


# Assitance from code institutes I think therefore I blog walkthrough tutorials
@admin.register(Todo)
class TodoAdmin(SummernoteModelAdmin):

    list_filter = ('title', 'due_date', 'created_on')
    list_display = ('title', 'due_date', 'completed', 'created_on')
    search_fields = ['title', 'details']
    summernote_fields = ('details')


# Assitance from code institutes I think therefore I blog walkthrough tutorials
@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):

    list_filter = ('city', 'postcode', 'created_on')
    list_display = ('client_id', 'city', 'postcode', 'created_on')
    search_fields = ['street', 'city', 'county', 'postcode']
