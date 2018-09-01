from django.contrib import admin
from portal.models import Absence

class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'from_date', 'to_date', 'approved')
    list_editable = ('approved',)
    list_filter = ('user','approved','type_miss', 'from_date')
    search_fields = ('from_date', 'to_date')


# Register your models here.
admin.site.register(Absence, AbsenceAdmin)