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
        context = self.get_home_page_data(request.user.id)
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
        # else:
        #     success = True
        context = self.get_home_page_data(request.user.id)
        return render(request, self.template_name, context)

    def get_home_page_data(self, user_id):
        today = dt.date.today()
        absences = Absence.objects.all().filter(from_date__lte=today, to_date__gte=today)
        my_absences = Absence.objects.filter(user=user_id).order_by('from_date')
        personal = Limit.objects.filter(user = user_id, year = yeld_year()).first()
        return {'absences': absences, 'my_absences': my_absences, 'personal': personal, 'form': self.form_class()}