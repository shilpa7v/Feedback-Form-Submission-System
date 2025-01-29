# Feedback-Form-Submission-System
This is a Django-based Feedback Collection System that allows users to submit feedback on various products. The system collects customer details, product selection, feedback messages, and satisfaction ratings.
1.Run this command in the terminal/console:

django-admin startproject feedback

2.cd feedback
3.python manage.py startapp form
4.Open the feedback/settings.py file and add ‘form’ in the INSTALLED_APPS list, like this:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'form',
]
5.python manage.py makemigrations
6.python manage.py migrate
7.python manage.py createsuperuser
8.python manage.py runserver
9.Now go to http://127.0.0.1:8000/admin/ from your browser

image

![Image](https://github.com/user-attachments/assets/182d1b33-2cc3-40e8-9080-827f0fb51eb4)








