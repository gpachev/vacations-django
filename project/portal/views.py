from django.shortcuts import render
from django.views import View
from portal.models import Limit, yeld_year
from portal.forms import SubmitForm
from django.contrib.auth.mixins import LoginRequiredMixin


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

        context = {
            'form': form,
            'personal': personal
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
            instance.save()
            form = self.form_class() #return pristine form
        return render(request, self.template_name, {'form': form})
