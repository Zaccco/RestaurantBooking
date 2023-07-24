from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('my_bookings/', views.my_bookings_page, name = 'my_bookings_page'),
    path('booking/', views.booking_page, name = 'booking_page'),
    path('edit/<booking_id>', views.edit_booking, name = 'edit'),
    path('delete/<booking_id>', views.delete_booking, name = 'delete'),
]