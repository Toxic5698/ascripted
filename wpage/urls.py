from django.urls import path
from .views import *

urlpatterns = [
    path('', WelcomePageMain.as_view(), name='home'),
    path('info', WelcomePageInfo.as_view(), name='info'),
    path('contact', WelcomePageContact.as_view(), name='contact')


    ]