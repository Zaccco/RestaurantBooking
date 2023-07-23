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


def booking_page(request):
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

def edit_booking(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('my_bookings_page')
    form = ReservationForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Reservation, id=booking_id)
    booking.delete()
    return redirect('my_bookings_page')