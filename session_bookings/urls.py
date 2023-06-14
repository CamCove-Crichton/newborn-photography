# Assitance from code institutes I think therefore I blog walkthrough tutorials
from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingList.as_view(), name='bookings'),
]
