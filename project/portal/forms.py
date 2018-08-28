from django import forms
from datetimewidget.widgets import DateTimeWidget

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
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian' : True,
            'attrs': {'id':"yourdatetimeid"}
        }

        widgets = {
            #Use localization and bootstrap 3
            'datetime': DateTimeWidget(options=dateTimeOptions)
        }