from django.shortcuts import render
from django.views import View
from portal.models import Limit, yeld_year, Absence
from portal.forms import SubmitForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime as dt


# Create your views here.
class HomeView(LoginRequiredMixin, View):
    """
    View for registering delays, vacations, sick days.
    """
    form_class = SubmitForm
    template_name = 'portal/form_template.html'

    def get(self, request, *args, **kwargs):
        
        form = self.form_class()
        personal = Limit.objects \
                        .filter(user = request.user) \
                        .filter(year = yeld_year()) \
                        .first()
        absences = get_current_absences()
        context = {
            'form': form,
            'personal': personal,
            'absences' : absences
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            #if the custom save method 
            # returns True, it is ok,
            # return False, pass ERROR to form
            success = instance.save()
            form = self.form_class() #return pristine form
        else:
            success = True
        personal = Limit.objects \
                .filter(user = request.user) \
                .filter(year = yeld_year()) \
                .first()
        absences = get_current_absences()
        return render(request, self.template_name, {"form": form, "success": success, 'absences': absences})

def get_current_absences():
    today = dt.date.today()
    absences = Absence.objects.all().filter(from_date__lte=today, to_date__gte=today)
    return absences
