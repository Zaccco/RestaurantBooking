from .models import Reservation
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'
    

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'time', 'guests', 'additional_info']
        widgets = {
            'date': DateInput()
        }