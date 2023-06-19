# Assitance from code institutes I think therefore I blog walkthrough tutorials
from . import views
from django.urls import path

# Assitance from code institutes I think therefore I blog walkthrough tutorials
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('<slug:slug>', views.BookingDetail.as_view(), name='booking_detail'),
    path('new_booking/', views.NewBooking.as_view(), name='new_booking'),
]
