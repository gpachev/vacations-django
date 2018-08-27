from django import forms
from django.contrib.admin import widgets

from .models import MissModel

VACATION = 'vacation'
DELAY = 'delay'

TYPE_CHOICES = (
    (VACATION, 'Vacation'),
    (DELAY, 'Delay')
)

class SubmitForm(forms.Form):
    from_date = forms.DateTimeField(widget=widgets.AdminSplitDateTime)
    to_date  = forms.DateTimeField(widget=widgets.AdminSplitDateTime)
    type_miss = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE_CHOICES)