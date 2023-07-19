from django.db import models
# Assitance from code institutes I think therefore I blog walkthrough tutorials
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Assitance from code institutes I think therefore I blog walkthrough tutorials
BOOKING_STATUS = ((0, "Not Confirmed"), (1, "Confirmed"))
SESSION_LOCATION = ((0, "Studio"), (1, "Home"))
BABYS_GENDER = ((0, "Unknown"), (1, "Male"), (2, "Female"))
USAGE_CONSENT = ((0, "No"), (1, "Yes"))

# Assitance from code institutes I think therefore I blog walkthrough tutorials


class Booking(models.Model):
    booking_name = models.CharField(max_length=250, unique=False)
    slug = models.SlugField(max_length=250, unique=False)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateField(auto_now=False, null=False)
    booking_time = models.TimeField(auto_now=False, default='10:00')
    babys_due_date = models.DateField(auto_now_add=False)
    babys_name = models.CharField(max_length=50, null=False, blank=False)
    babys_gender = models.IntegerField(choices=BABYS_GENDER, default=0)
    location = models.IntegerField(choices=SESSION_LOCATION, default=0)
    special_requests = models.TextField(null=True, blank=True)
    how_you_found_me = models.CharField(max_length=250, null=True, blank=True)
    consent = models.IntegerField(choices=USAGE_CONSENT, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=BOOKING_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.booking_name


class Todo(models.Model):
    booking_id = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name="todo")
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=False)
    details = models.TextField(null=True, blank=True)
    due_date = models.DateField(auto_now=False, blank=True, default=None)
    due_time = models.TimeField(auto_now=False, blank=True, default='12:00')
    created_on = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"Item: {self.title}, Complete by: {self.due_date}"
