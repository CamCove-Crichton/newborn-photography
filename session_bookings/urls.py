# Assitance from code institutes I think therefore I blog walkthrough tutorials
from . import views
from django.urls import path

# Assitance from code institutes I think therefore I blog walkthrough tutorials
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('bookings/<slug:slug>/<int:id>',
         views.BookingDetail.as_view(), name='booking_detail'),
    path('new_booking/', views.NewBooking.as_view(), name='new_booking'),
    path('edit_booking/<slug:slug>/<int:id>',
         views.EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<slug:slug>/<int:id>',
         views.DeleteBooking.as_view(), name='delete_booking'),
    path(
        'admin-panel/', views.AdministratorView.as_view(), name='admin_panel'),
    path('bookings/<slug:slug>/<int:id>/new_todo/',
         views.NewTodo.as_view(), name='new_todo'),
    path('todo_item/<slug:slug>/<int:id>/',
         views.TodoDetail.as_view(), name='todo_detail'),
    path('edit_todo/<slug:slug>/<int:id>/',
         views.EditTodo.as_view(), name='edit_todo'),
]
