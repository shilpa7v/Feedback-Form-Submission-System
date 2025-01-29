from django.urls import path  # Import path instead of url
from . import views

app_name = 'form'
urlpatterns = [
    path('', views.feedback_form, name='home'),  # Use path() instead of url()
]
