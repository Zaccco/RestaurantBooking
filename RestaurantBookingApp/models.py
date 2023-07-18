from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):

    TIME_OPTIONS = (
        ('11:00', '11:00'),
        ('11:30', '11:30'),
        ('12:00', '12:00'),
        ('12:30', '12:30'),
        ('13:00', '13:00'),
        ('13:30', '13:30'),
        ('14:00', '14:00'),
        ('14:30', '14:30'),
        ('15:00', '15:00'),
        ('15:30', '15:30'),
        ('16:00', '16:00'),
        ('16:30', '16:30'),
        ('17:00', '17:00'),
        ('17:30', '17:30'),
        ('18:00', '18:00'),
        ('18:30', '18:30'),
        ('19:00', '19:00'),
        ('19:30', '19:30'),
        ('20:00', '20:00'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_booking")
    first_name = models.CharField("First name", max_length=20)
    last_name = models.CharField("Last name", max_length=30)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    guests = models.IntegerField("Number of people")
    date = models.DateField()
    time = models.CharField("Arrival time", max_length=30, choices=TIME_OPTIONS, default="18:00")
    additional_info = models.TextField("Please provide any speciel requests or allergies", blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

