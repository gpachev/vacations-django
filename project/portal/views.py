from django.shortcuts import render
from django.views import View
from portal.forms import SubmitForm

# Create your views here.
class HomeView(View):
    form_class = SubmitForm
    template_name = 'portal/main_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, {'form': form})
