from django import forms

from .models import Absence

VACATION = 'vacation'
DELAY = 'delay'
SICK = 'sick'

TYPE_CHOICES = (
    (VACATION, 'Vacation'),
    (DELAY, 'Delay'),
    (SICK, 'Sick')
)

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ("from_date", "to_date", "type_miss")
        widgets = {
            'from_date': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'to_date': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'type_miss': forms.Select(attrs={'class': 'form-control', 'required': True})
        }