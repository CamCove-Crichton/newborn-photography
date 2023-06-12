# Newborn Photography Hub

## A newborn photography bookings site, where users can create an account, login and create, view, edit or cancel photoshoot bookings for their newborn babies, and the photographer is able to see all the sessions booked in from an admin perspective and if needed, can create, view, edit or delete any Todo items required for the photo sessions

### Features

- User Sign Up/Login
- Create, View, Edit or Delete session bookings
- Photographer Administrator site to view booked sessions & create Todo list per booking

## Deployment

*website links go here*

- Installed required technologies for the bare bones of the project, Django, Cloudinary, PostgreSQL & Psycopg2
- Added these to the requirements.txt file
- Created a new Django project "newborn_photography"
- Created a new app called "session_bookings"
- Added the newly created app to the 'Installed Apps' section in the settings file
- Migrated the changes to the "manage.py" file
- Created a new app on Heroku
- Created a new PostgreSQL Database Instance using ElephantSQL
- Added an env.py file and setup my environment variables
- Updated the settings.py file to be able to check for the env.py file & updated the secret key
- Hooked up the created database to project within the settings file
- Migrated the changes to the manage.py file
- Added the config vars to my heroku app
- Added Cloudinary to the env.py file to link my cloudinary account
- Added Cloudinary to the config vars in my Heroku app
- Added Disable Collectstatic as a config var to the Heroku app as a temporary measure until the static files are setup
- Added the cloudinary_storage and cloudinary libraries to the installed apps in the settings file
- Assigned the cloudinary_storage library to STATICFILES_STORAGE constant
- Setup the static directory using STATIC_DIRS as the constant
- Setup the static root using STATIC_ROOT as the constant
- Setup a media url using MEDIA_URL as the constant
- Set the MediaCloudinaryStorage to DEFAULT_FILE_STORAGE
- Added TEMPLATES_DIR to inform django where my templates will be stored
- Updated the DIRS key on the templates setting to point to the TEMPLATES_DIR constant
- Add the Heroku host name to the allowed hosts in settings
- Create the media, static and templates directories
- Create a Profile
- Deployed app with Heroku through Github

*Forking & Cloning goes here*

### Am I Responsive

*screengrab goes here*

## Development

- Began by going through all the settings and installing the required libraries to get my project deployed to heroku (Listed deployment steps above)
- Started working on the first model, called Booking in the models.py file which will handle all the booking information required for the database
- Created the Todo model to handle all the Todo items required for a particular booking
- Created the Personal Info model to handle all the personal details for the client/user, like the Address and Contact number
- Made the mirgrations using the command line interface, and migrated the models
- Created a superuser for the Django admin panel
- Installed Summernote for WYSIWYG editor for the Special Requests in the Admin panel
- Linked up Summernote in settings and URLs files and added a class in the Admin file to assign the fields to the summernote_fields list
- Migrated the changes, and updated the BookingAdmin properties to get the slug field to auto populate with the name of the booking name
- Added in the properties to enable filtering and searches on the Admin panel
- Updated the Todo model to add a Slug Field to assist with unique URLs for each todo item created
- added the Todo model to the list of imports in the admin file to be able to view it within the Admin panel
- Made migrations and migrated the models to update the database
- Updated some of the field in the models to ensure certain fields are marked are required and cannot be empty programatically
- Imported the Personal Info model into the Admin file and registered it to display in the Django admin panel
- Add a method to allow the admin to be able to approve requested bookings
- Updated the Todo model so the due date and details fields are not mandatory and can be left blank
- Made the mirgrations and migrated the changes to the database

### Future Developments

- To allow users to be able to have confirmed appointments without the need for the Admin to approve

### Wireframes & Database Designs

*Wireframes go here*
*Database Designs go here*

### Technologies

- Django
- Gunicorn
- Cloudinary
- PostgreSQL
- dj-database-url
- Psycopg2

### Finished Site Screen Grabs

## Testing

*Manual Testing Goes here*
*Include Responsiveness, Browser compatibility, resolved bugs, unresolved bugs, Lighthouse, code validation, User Stories Testing, Features Testing*
**Remember to make the manual testing write-up visual! - Share Test cases, uses tables where appropriate, and include screenshots where possible!**

### Resolved Bugs

*List of resolved bugs goes here*

### Validator Testing

*W3C Nu HTML Checker*
*W3C Jigsaw CSS Validator*
*JS Hint Validator*
*PEP8 Python Validator*
*Lighthouse perfromace check*

### Unresolved Bugs

*List of any unresolved bugs goes here*

## Credits

### Code

[Code Institute](https://codeinstitute.net/) - Used below code in my project from the I think therefore I blog video tutorials

```python
{
    from django.contrib.auth.models import User
    from cloudinary.models import CloudinaryField
}
```

```python
{
    BOOKING_STATUS = ((0, "Not Confirmed"), (1, "Confirmed"))
    SESSION_LOCATION = ((0, "Studio"), (1, "Home"))
    BABYS_GENDER = ((0, "Unknown"), (1, "Male"), (2, "Female"))
    USAGE_CONSENT = ((0, "No"), (1, "Yes"))
}
```

```python
{
    class Booking(models.Model):
        booking_name = models.CharField(max_length=250, unique=True)
        slug = models.SlugField(max_length=250, unique=True)
        client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
        booking_date = models.DateTimeField(auto_now=False)
        babys_due_date = models.DateField(auto_now_add=False)
        babys_name = models.CharField(max_length=50)
        babys_gender = models.IntegerField(choices=BABYS_GENDER, default=0)
        location = models.IntegerField(choices=SESSION_LOCATION, default=0)
        special_requests = models.TextField()
        how_you_found_me = models.CharField(max_length=250)
        consent = models.IntegerField(choices=USAGE_CONSENT, default=0)
        updated_on = models.DateTimeField(auto_now=True)
        featured_image = CloudinaryField('image', default='placeholder')
        created_on = models.DateTimeField(auto_now_add=True)
        status = models.IntegerField(choices=BOOKING_STATUS, default=0)

        class Meta:
            ordering = ['-created_on']
    
        def __str__(self):
            return self.booking_name
}
```

```python
{
    from .models import Booking
}
```

```python
{
    from django.urls import path, include
}
```

```python
{
    path('summernote/', include('django_summernote.urls')),
}
```

```python
{
    from django_summernote.admin import SummernoteModelAdmin
}
```

```python
{
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
}
```

```python
{
    @admin.register(Todo)
    class TodoAdmin(SummernoteModelAdmin):

        prepopulated_fields = {'slug': ('title',)}
        list_filter = ('title', 'due_date', 'created_on')
        list_display = ('title', 'due_date', 'completed', 'created_on')
        search_fields = ['title', 'details']
        summernote_fields = ('details')
}
```

```python
{
    @admin.register(PersonalInfo)
    class PersonalInfoAdmin(admin.ModelAdmin):

        prepopulated_fields = {'slug': ('client_id',)}
        list_filter = ('city', 'postcode', 'created_on')
        list_display = ('client_id', 'city', 'postcode', 'created_on')
        search_fields = ['street', 'city', 'county', 'postcode']
}
```

### Other Credits

[Code Institute](https://codeinstitute.net/) - Used for the below assistance

- I think therefore I blog video tutorials for assistance with initial deployment
