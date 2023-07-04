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
- Update the view booking url to include the id, and create a new view and url and template to start the process to enable users to edit their bookings
- Completed the view code to enable booking edits and to update the database with edited info
- Added in a cancel button on the new booking request form, so users can cancel the bookings request if they no longer wish to make a booking request
- Created a script.js file for my custon JavaScript, and linked up both my style.css and script.js files in the base.html file, and added a bit of custom css to ensure it is wired up correctly and added an event listener to my script.js file to infom when the DOM content is loaded and to ensure my script.js file is wired up correctly
- Updated the base.html file with a jQuery CDN script to utilise jQuery within my JavaScript code
- Began working on implementing some defensive programming for cancel and delete buttons on the site by adding a deleteModal function in the script.js file
- Updated the deleteModal function to display the modal when the cancel button is clicked to confirm the cancellation request before actually confirmation the cancellation and redirecting to the bookings page
- Finished updating the deleteBooking view and updated the booking_detail template to display the modal to confirm the deletion of the booking before deleting the record from the database, so effectively adding my defensive programming to both the cancel and delete buttons
- Created an Administrator view, so the Admin can login to the site and have access to the Client Bookings. Essentially where the client can manage the admin side of things, and where they will be able to add Todo items for each individual booking but where they can see all the bookings made by any of the clients signed up to the site
- Added in a NewTodo view for the Admin to have access to, when viewing the booking detail, so they can add a todo item for thet particluar booking for anything the Admin may need to action before the photo session
- Updated the BookingDetail view to enable displaying the todo items within the template, and updated the booking_detail.html template to iterate through todo items added to the booking and only display them if the user logged in is the Admin
- Added in a view and created a template for the admin to view the full details of a todo item, and gave it the url path using the slug and the id
- Added in a view to enable the admin to edit the todo items and created a url path and a template for the view

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
- jQuery

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
- Had an issue with the AdministratorView or at the time AdministratorPanelView not being defined in my urls.py file, and I realised that it was because I had not added the 'views.' to the front of my class name
- Struggled with getting the view to actually display what I was intending for it to display, and tried different decorators on my AdministratorView and thought I needed one then for my Home view but I then realised it was the fine with just a method_decorator on the AdministratorView and using a control statement in my administrator_panel.html template to check is the user thet is logged in is a superuser
- I had a 400 Bad Request error displaying then and realised I had left off a '%' in my control statement which then fixed the issue
- I struggled to get the template to iterate through all the bookings with the code in my AdministratorView, and found out more about the generic.ListView from django, that I do not need to have a get method, as this is built in with the ListView, and also learnt that the get_queryset() also gets all the objects that is assigned to the model attribute, and so did not have to decalare a variable "bookings = Booking.objects.all()", and that I could use the get_queryset() method and overide it with the parent class using super() to then do things like hpw to display the objects, and with assigning context_object_name, I could use this in my control statement in my administrator_panel.html template to iterate through the objects and display them by booking date
- Had a error to say Todo was not defined when creating my TodoForm, and realised I had not imported the Todo model, so imported the Todo model and it was cleared
- Had the same error when defining my view as well as the TodoForm was not defined, so I imported both the Todo model and the TodoForm and the errors were cleared
- Had an issue with getting the new_todo template displaying. I kept getting a NoReverseMatch error for the url I had input for the href in the confirmation for cancelling the new todo item, as it could not find the id & slug in which I was asking it to return to, until I decided to send it back to the bookings template, which solved the issue for the time being
- I then had an issue with the form submitting to the database and it was because it was not assiging the slug and id, so I needed to needed to assign a booking_id and a booking_slug so it could be associated with a particular booking, before using the get_object_or_404() method. After getting this from the Booking model, I assigned it to an attribute called 'booking'. Using 'booking', I then assigned it to the new todo item, and used slugify to convert the title of the todo to the slug before saving it, which solved the issue to a point, but when it was trying to post to the database, it was still not able to access the booking id and the slug to which it was related to, so in the get method of the NewTodo view, I did a similar thing, where I assigned attributes slug and booking_id the values of url parameters, and using the queryset attribute, I got all the objects from the Booking model, and then assigning the attribute 'booking' in the get method, using the get_object_or_404() method by the accessing the queryset and using the slug and booking_id as arguments, which solved this side of the issue
- The last issue was back to the NoReverseMatch again, and realised I had not updated the href in my booking_detail template to match the url path, and once I updated this, it posted to the database
- Had another issue with accessing the todo_detail template from the booking_detail template, and found that I was not actually looking at how django was trying to access the url, as I kept getting the NoReverseMatch so it was not getting the id and the slug values of the record, and found that because I was actually in the BookingDetail view, I was using the wrong naming for accessing the todo item, as in the BookingDetail view, the context was being accessed by "todos", and so I adjusted the arguments for the url path, and django was able to access the slug and the id

### Validator Testing

*W3C Nu HTML Checker*
*W3C Jigsaw CSS Validator*
*JS Hint Validator*
*PEP8 Python Validator*
*Lighthouse perfromace check*

### Unresolved Bugs

- I have an issue with the cnacel button, that it is not responsive on the first click, but only on the 2ns click, so need to look into this and correct

## Credits

### Code

[Techie Delight](https://www.techiedelight.com/) - Used to remind myself how to ensure my DOM content is loaded before my JavaScript runs

```javascript
{
    document.addEventListener("DOMContentLoaded", function () {
        console.log('Page is loaded');
    });
}
```

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

```javascript
{
    function deleteModal(targetModal) {
    let deleteButtons = document.getElementsByClassName("deleteBtn");

    for (let deleteButton of deleteButtons) {
        deleteButton.addEventListener("click", handleDeleteButtonClick.bind(null, targetModal), { once: true });
    }

    function handleDeleteButtonClick(targetModal) {
        console.log("Delete button clicked");
        let modal = document.querySelector(targetModal);
        $(modal).modal("show");
    }
}
}
```

```python
{
    from django.contrib.admin.views.decorators import staff_member_required
    from django.utils.decorators import method_decorator
}
```

```python
{
    # Assitance from Code Institutes I thing therefore I blog walkthrough tutorials and ChatGpt
    @method_decorator(staff_member_required(login_url='account_login'), name='dispatch')
    class AdministratorView(generic.ListView):

        model = Booking
        template_name = 'administrator_panel.html'
        paginate_by = 6
        context_object_name = 'bookings'

        def get_queryset(self):
            return super().get_queryset().order_by('booking_date')
}
```

```python
{
    path('admin-panel/', views.AdministratorView.as_view(), name='admin_panel'),
}
```

```html
{
    {% for booking in bookings %}
}
```

```html
{
    {% if user.is_superuser %}
}
```

```python
{
    class NewTodo(LoginRequiredMixin, generic.ListView):
    """
    The NewTodo class is to create a view for superusers to fill in a todo form
    and submit it to add to a list of todo items related to that booking
    """
    model = Todo
    form_class = TodoForm

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials & ChatGpt
    def get(self, request, *args, **kwargs):
        """
        Fetches the content to display from the TodoForm() which uses
        crispy forms and is located in the forms.py file
        """

        # Get the slug and id from the URL parameters
        slug = self.kwargs['slug']
        booking_id = self.kwargs['id']

        # Retrieve the booking object based on the slug and id
        queryset = Booking.objects.all()
        booking = get_object_or_404(queryset, slug=slug, id=booking_id)

        return render(
            request,
            "new_todo.html",
            {
                "form": TodoForm(),
                "booking": booking,
            },
        )

    # Assitance from code institutes I think therefore I blog walkthrough
    # tutorials & ChatGpt

    def post(self, request, *args, **kwargs):
        """
        Submits the new todo item, when it is valid, to the database
        """

        form = TodoForm(request.POST)

        if form.is_valid():
            todo_item = form.save(commit=False)

            # Get the booking related to the todo item
            booking_slug = request.POST['slug']
            booking_id = request.POST['id']
            booking = get_object_or_404(
                Booking, slug=booking_slug, id=booking_id)

            # Set the booking_id and slug for the todo item
            todo_item.booking_id = booking
            todo_item.slug = slugify(todo_item.title)

            todo_item.save()

            return redirect('booking_detail', slug=booking_slug, id=booking_id)
        else:
            return render(
                request,
                "new_todo.html",
                {
                    "form": form
                },
            )
}
```

```html
{
    <input type="hidden" name="slug" value="{{ booking.slug }}">
    <input type="hidden" name="id" value="{{ booking.id }}">
}
```

```python
{
    booking = get_object_or_404(Booking, slug=slug)
    todos = Todo.objects.filter(booking_id=booking)
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

```python
{
    class TodoDetail(View):
        """
        TodoDetail class gets all the details about a todo item to display it to the admin
        """

        def get(self, request, slug, id):
            # Assistance from ChatGpt
        
            todo_item = get_object_or_404(Todo, slug=slug, id=id)

            return render(
                request,
                "todo_detail.html",
                {
                    "todo_item": todo_item
                },
            )
}
```

```python
{
    booking = todo_item.booking_id

        form = TodoForm(instance=todo_item)
        context = {
            "form": form,
            "booking_slug": booking.slug,
            "booking_id": booking.id
        }
}
```

```python
{
    booking_slug = todo_item.booking_id.slug
    booking_id = todo_item.booking_id.id
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

```python
{
    class EditBooking(LoginRequiredMixin, generic.ListView):
    """
    The EditBooking class is to create a view for users to be able to edit their booking details
    """
    model = Booking

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def get(self, request, *args, **kwargs):
        """
        Fetches the content to display from the BookingForm() which uses
        crispy forms and is located in the forms.py file
        """
        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
        context = {
            "form": form
        }

        return render(request, "edit_booking.html", context)

    # Assitance from code institutes I think therefore I blog walkthrough tutorials
    def post(self, request, *args, **kwargs):
        """
        Submits the new booking request, when it is valid, to the database
        """

        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
        context = {
            "form": form
        }

        update_booking = BookingForm(
            request.POST, request.FILES, instance=booking)

        # Assitance from code institutes I think therefore I blog walkthrough tutorials & ChatGpt
        if update_booking.is_valid():
            booking = update_booking.save(commit=False)
            booking.client = request.user
            booking.slug = slugify(booking.booking_name)
            booking.featured_image = update_booking.cleaned_data['featured_image']
            booking.save()
            return redirect('bookings')
        else:
            return render(request, "edit_booking.html", context)
}
```

```python
{
    class DeleteBooking(LoginRequiredMixin, generic.ListView):
    """
    The DeleteBooking class is to enable users to delete one of thier bookings
    """
    model = Booking

    def get(self, request, *args, **kwargs):
        """
        Fetches the content to delete a record from the database which uses the booking id
        """
        booking_id = kwargs['id']
        booking = get_object_or_404(Booking, id=booking_id)
        form = BookingForm(instance=booking)
        context = {
            "form": form
        }

        booking.delete()

        return redirect('bookings')
}
```

### Other Credits

[Code Institute](https://codeinstitute.net/) - Used for the below assistance

- I think therefore I blog video tutorials for assistance with initial deployment

[ChatGPT](https://openai.com/blog/chatgpt) - Used ChatGPT for questions and queries in a similar manner as to using google

[Google](https://www.google.com/) - Used Google to do searches on any issues or questions to troubleshoot, remind myself or teach myself

[Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Used Bootstrap documentation to read up on how to implement and use certain classes and elements

[Stack Overflow](https://stackoverflow.com/) - Used stack overflow when troubleshooting issues
