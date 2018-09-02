from django.shortcuts import render
from django.views import View
from portal.forms import SubmitForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomeView(LoginRequiredMixin, View):
    
    form_class = SubmitForm
    template_name = 'portal/form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user.id
            instance.save()
            form = self.form_class() #return pristine form
        return render(request, self.template_name, {'form': form})
