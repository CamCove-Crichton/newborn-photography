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
- Began working on the views by creating a class based view to display all Bookings
- Created a base.html file to use to extend all other html pages from as well as the bookings.html file where clients/users will be able to view all their bookings when logged in
- Created a css directory and a style.css file for the styling of the site
- Setup the head of my base.html file using boilerplate html, and adding in a couple extra meta tags for seo purposes
- Added in the link tags for the fonts for the site, using Oswald and Simonetta from Google Fonts
- Added in my script tag for my Font Awesome kit
- Added the bootstrap link tag to the head of my base.html file and then added the bootstrap script tag just before the closing body tag in the base.html file
- Began by adding in the header element, with a nav element nested in the header
- Added a main element to insert the main content which will be extended in the other files
- Then added a footer element as a placeholder for items like the social media link etc.
- Began working on the header section in the base.html file for the heading and site navigation as well as the signup/login feature
- Created an index.html file to be used as the home page and extended both the index.html file and the bookings.html file from the base.html file
- Added in the social links and font awesome icons in the footer section of the base.html file
- Began working a bit on the content layout for the bookings.html page
- Then wired up the bookings page as the default page to test it out
- Continued updating the bookings page to view an image using bootstrap features and uploading an image to cloudinary and using the url for the default booking image if an image has not been provided by the client/user
- Added in a button to the bookings page to request a new booking, and added a new_booking.html file which extends from the base.html file
- Added in a control statement to display a message if there are no existing bookings on the bookings page for the client/user to view
- Added a booking detail file to be able to view all the details about the booking
- Added a new view to have the index.html file be the home page and switch the bookings page to the bookings link
- Added a new view and wired up the URL to enable a new booking request view
- Installed allauth to enable authentication for signup and logins and added it to the requirements file and then added it to the list of installed apps in the settings.py file and included the allauth URLs in the projects urls file
- Created a site id to tell django the site id, so it can handle multiple sites and created login and logout redirects in the settings file and then ran the mirgrations
- Updated the base.html with the href urls for the signup, login and logout buttons
- Copied across the account template files from django into my project, and then adjusted the signup, login and logout html templates to extend from my base.html file
- Created the basic layout for the new booking request form
- Updated the bookings page and bookings detail page with some control statements to display the choices in a human readable format
- Updated the general layout/look of the signup, login and logout pages with a few bootstrap classes
- Installed Django Crispy Forms to assist with the flexibility and customization of the forms and updated the requirements.txt file
- Updated the setting file to add crispy forms to the installed apps
- Created a forms file for form classes to utilise crispy forms when adding the form to the class based view in the views.py file, then proveeded to update the new booking template accordingly to utilise crispy forms
- Got the new booking request to submit and to save to the database using slugify to covert the bookiing name to a slug and assign it to the slug field in the model as well as assign the uploaded file to the featured image field in the database
- Update the BookingList view to display only the currently logged in user's bookings to the user
- I decided to update the Booking model to separate the booking date and time into their own fields, and display them in the form as separate inputs
- I also imported redirect from django shortcuts in my views.py file to redirect to the bookings.html template once a new booking request form has been submitted
- Updated the New Booking Request form class to accept the date format in a day-month-year format and the widgets format to render the date in a day-month-year format

### Future Developments

- To allow users to be able to have confirmed appointments without the need for the Admin to approve
- To allow users to signup or login using social media accounts
- To allow users to reset their password if they cannot remember their existing password
- To have users receive an authentication email when signing up to validatate their email address

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
- Bootstrap
- Django allauth
- Django Crispy Forms

### Finished Site Screen Grabs

## Testing

*Manual Testing Goes here*
*Include Responsiveness, Browser compatibility, resolved bugs, unresolved bugs, Lighthouse, code validation, User Stories Testing, Features Testing*
**Remember to make the manual testing write-up visual! - Share Test cases, uses tables where appropriate, and include screenshots where possible!**

### Resolved Bugs

- Corrupted database, had to delete the inital database and update the models, and then made the migrations again and migrated the database to rectify the issue
- Could not connect up the index.html view and realised I was using the url of the file and not the assigned name for the url in the control statement
- Was unable to get my bookings view to diplay and found that when the initial new booking request was posted to the database that it was without a slug and so it was causing an error
- The initial route of the slug field being assigned a value was incorrect and so was returning a str which was an invalid value, so I used slugify to use the booking name and create a slug for the booking request before it gets saved
- The featured image is being assigned the uploaded file, but is currently not displaying when viewing the template, but instead the alt attribute value is displayed - I found that there was a typo in my template that was missing the 'r' in url, so it is displaying correctly now

### Validator Testing

*W3C Nu HTML Checker*
*W3C Jigsaw CSS Validator*
*JS Hint Validator*
*PEP8 Python Validator*
*Lighthouse perfromace check*

### Unresolved Bugs

- None that I have found

## Credits

### Code

[ChatGpt](https://openai.com/blog/chatgpt) - Asked ChatGpt if it was possible to assign the context for a view to my BookingForm class to utilise crispy forms, to which I was told yes but the preffered way to do it was the below

```pyton
{
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm()
        return context
}
```

```html
{
    <form method="post" enctype="multipart/form-data">
}
```

```python
{
    # Assitance from code institutes I think therefore I blog walkthrough tutorials & ChatGpt
        if new_booking_request.is_valid():
            booking = new_booking_request.save(commit=False)
            booking.client = request.user
            booking.slug = slugify(booking.booking_name)
            booking.featured_image = new_booking_request.cleaned_data['featured_image']
            booking.save()
            return render(request, "bookings.html")
        else:
            return render(
                request,
                "new_booking.html",
                {
                    "form": BookingForm()
                },
            )
}
```

```python
{
    class BookingList(LoginRequiredMixin, generic.ListView):
}
```

```python
{
    user = self.request.user
        queryset = super().get_queryset().filter(client=user).order_by('-booking_date')

        return queryset
}
```

```python
{
    booking_date = forms.DateField(
        input_formats=['%d-%m-%y', '%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%y'),)
    babys_due_date = forms.DateField(
        input_formats=['%d-%m-%y', '%d-%m-%Y'], widget=forms.DateInput(format='%d-%m-%y'),)
}
```

[Bootstrap](https://getbootstrap.com/) - Used Bootstrap to assist with styling

```html
{
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
}
```

```html
{
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
        crossorigin="anonymous"></script>
}
```

[Font Awesome](https://fontawesome.com/) - Used Font Awesome for any icons required in the project

[Google Fonts](https://fonts.google.com/) - Used the Oswald & Simonetta fonts from Google Fonts

```html
{
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Oswald:wght@200;300;400;500;600;700&family=Simonetta:ital,wght@0,400;0,900;1,400;1,900&display=swap"
        rel="stylesheet">
}
```

[Code Institute](https://codeinstitute.net/) - Used below code in my project from the I think therefore I blog video tutorials as well as the Hello Django video tutorials

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
    path('accounts/', include('allauth.urls')),
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

```python
{
    from django.views import generic
    from .models import Booking
}
```

```python
{
    class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by('-booking_date')
    template_name = 'bookings.html'
    paginate_by = 6
}
```

```html
{
    {% load static %}
}
```

```html
{
    <main>
        {% block content %}
        <!-- Main content goes here -->
        {% endblock content %}
    </main>
}
```

```html
{
    <div>
            {% if user.is_authenticated %}
            <a href="#">{{ user.first_name }}</a>
            {% else %}
            <a href="#">Signup/Login</a>
            {% endif %}
        </div>
}
```

```html
{
    <ul>
                    <li>
                        <a href="#">Home</a>
                    </li>
                    <li>
                        <a href="#">Blogs</a>
                    </li>
                    <li>
                        <a href="#">Gallery</a>
                    </li>
                    <li>
                        <a href="#">Contact</a>
                    </li>
                    {% if user.is_authenticated %}
                    <li>
                        <a href="#">Bookings</a>
                    </li>
                    {% endif %}
                </ul>
}
```

```html
{
    {% extends "base.html" %}
}
```

```html
{
    {% block content %}
    <div class="container-fluid">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-3">
                    <a href="#" type="button" class="btn btn-success">New Booking</a>
                </div>
            </div>
        </div>
        <div class="row">
            <!-- Bookings column -->
            <div class="col-12 mt-2">
                <div class="row">
                    {% for booking in booking_list %}
                    <div class="col-md-4">
                        <div class="card mb-2">
                            <div class="card-body">
                                <div class="image-container">
                                    {% if "placeholder" in booking.featured_image.url %}
                                    <img src="https://res.cloudinary.com/dvvi4mkst/image/upload/v1686808069/baby_hug4bo.jpg"
                                        alt="default booking image" class="card-image-top">
                                    {% else %}
                                    <img src="{{ booking.featured_image.ul }}" alt="custom booking image"
                                        class="card-image-top">
                                    {% endif %}
                                    <div class="card-text">
                                        <a href="{% url 'booking_detail' booking.slug %}">
                                            <h4>{{ booking.babys_name}}'s Newborn Shoot</h4>
                                            <p>Booking: {{ booking.booking_date }}</p>
                                            <p>Location: {{ booking.location }}</p>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {% if forloop.counter|divisibleby:3 %}
                </div>
                <div class="row">
                    {% endif %}
                    <!-- Assitance from code institutes Hello Django walkthrough tutorials -->
                    {% empty %}
                    <div class="container-fluid">
                        <p>You currently have no bookings</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
        {% if is_paginated %}
        <nav aria-label="Page navigation">
            <ul class="pagination justify-content-center">
                {% if page_obj.has_previous %}
                <li><a href="?page={{ page_obj.previous_page_number }}" class="page-link">&laquo; PREV </a></li>
                {% endif %}
                {% if page_obj.has_next %}
                <li><a href="?page={{ page_obj.next_page_number }}" class="page-link"> NEXT &raquo;</a></li>

                {% endif %}
            </ul>
        </nav>
        {% endif %}
    </div>

    {% endblock content %}
}
```

```python
{
    from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingList.as_view(), name='bookings'),
    path('<slug:slug>', views.BookingDetail.as_view(), name='booking_detail'),
]
}
```

```python
{
    path('', include('session_bookings.urls'),
         name='session_bookings_urls'),
}
```

```python
{
    class BookingDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Booking.objects
        booking = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "booking_detail.html",
            {
                "booking": booking
            },
        )
}
```

```python
{
    class Home(View):
    def get(self, request):
        return render(request, "index.html")
}
```

```python
{
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
}
```

```python
{
    SITE_ID = 1

    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/'
}
```

```python
{
    ACCOUNT_EMAIL_VERIFICATION = 'none'
}
```

```html
{
    <li>
        <a href="{% url 'account_logout' %}">Logout</a>
    </li>
}
```

```html
{
    <li>
        <a href="{% url 'account_signup' %}">Signup</a>
    </li>
    <li>
        <a href="{% url 'account_login' %}">Login</a>
    </li>
}
```

```html
{
    <div class="container">
    <div class="row">
        <div class="col-md-8 mt-3 offset-md-2"></div>
    </div>
</div>
}
```

```python
{
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
}
```

```python
{
    from .models import Booking
    from django.contrib.auth.models import User
    from django import forms


    class BookingForm(forms.ModelForm):
        class Meta:
            model = Booking
            fields = ('booking_name', 'booking_date', 'babys_due_date', 'babys_name', 'babys_gender',
                        'location', 'special_requests', 'how_you_found_me', 'consent', 'featured_image', 'status',)
}
```

```html
{
    {% load_crispy_forms_tags %}
}
```

```html
{
    {{ booking_form | crispy }}
    {% csrf_token %}
}
```

```python
{
    redirect('bookings')
}
```

### Other Credits

[Code Institute](https://codeinstitute.net/) - Used for the below assistance

- I think therefore I blog video tutorials for assistance with initial deployment

[ChatGPT](https://openai.com/blog/chatgpt) - Used ChatGPT for questions and queries in a similar manner as to using google

[Google](https://www.google.com/) - Used Google to do searches on any issues or questions to troubleshoot, remind myself or teach myself

[Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Used Bootstrap documentation to read up on how to implement and use certain classes and elements

[Stack Overflow](https://stackoverflow.com/) - Used stack overflow when troubleshooting issues
