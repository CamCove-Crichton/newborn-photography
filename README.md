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

*Forking & Cloning goes here*

### Am I Responsive

*screengrab goes here*

## Development

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

*coding credits goes here*

### Other Credits

[Code Institute](https://codeinstitute.net/) - Used for the below assistance

- I think therefore I blog video tutorials for assistance with initial deployment
