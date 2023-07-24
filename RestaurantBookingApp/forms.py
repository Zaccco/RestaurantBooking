from .models import Reservation
from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    

class ReservationForm(forms.ModelForm):
    class Meta:
        """
        Decides the format of the booking form
        """
        model = Reservation
        fields = ['date', 'time', 'guests', 'additional_info']
        widgets = {
            'date': DateInput()
        }
    
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date