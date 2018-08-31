from django import forms

from .models import MissModel

VACATION = 'vacation'
DELAY = 'delay'

TYPE_CHOICES = (
    (VACATION, 'Vacation'),
    (DELAY, 'Delay')
)

# class SubmitForm(forms.Form):
#     from_date = forms.DateTimeField(widget=widgets.AdminSplitDateTime)
#     to_date  = forms.DateTimeField(widget=widgets.AdminSplitDateTime)
#     type_miss = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE_CHOICES)

class SubmitForm(forms.ModelForm):
    class Meta:
        model = MissModel
        fields = ("from_date", "to_date", "type_miss")
        widgets = {
            'from_date': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'to_date': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'type_miss': forms.Select(attrs={'class': 'form-control', 'required': True})
        }