from django import forms
from portal.models import Absence

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ("from_date", "to_date", "type_miss", "comment")
        widgets = {
            'from_date': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'to_date': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'type_miss': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'required': False})
        }