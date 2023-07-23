from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Reservation
from django.contrib import messages
from .forms import ReservationForm


# Create your views here
def home(request):
    """
    This is the view for the homepage that renders index.html
    """
    return render(request, 'index.html')


def booking_page():
    """
    The view for the booking page. If the user is logged in, the my bookings page
    will show up, if the user is not logged in, it will be redirected to the
    login/signup page.
    """
    if request.method == 'POST':
        form = ReservationForm(data=request.POST)
        if form.is_valid():
            reservation_form = form.save(commit=False)
            reservation_form.user = request.user
            reservation_form.save()
            messages.success(request, 'Booking succeeded!')
            return redirect('my_bookings_page')
        else:
            messages.error(
                request, 'Inavlid info'
            )
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)


def my_bookings_page(request):
    if request.user.is_authenticated:
        bookings = Reservation.objects.filter(user=request.user)
        context = {
            'bookings': bookings
        }
        return render(request, 'mybookings.html', context)
    else:
        return redirect('../accounts/signup')