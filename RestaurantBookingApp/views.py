from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Reservation
from django.contrib import messages


# Create your views here.
def home(request):
    """
    This is the view for the homepage that renders index.html
    """
    return render(request, 'index.html')


def booking_page():
    """
    The view for the booking page. If the user is logged in the bookings page
    will show up, if the user is not logged in, it will be redirected to the
    login/signup page.
    """
    pass