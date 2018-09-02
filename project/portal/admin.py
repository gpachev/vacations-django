from django.contrib import admin
from portal.models import Absence, Limit

class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'from_date', 'to_date', 'approved')
    list_editable = ('approved',)
    list_filter = ('user','approved','type_miss', 'from_date')
    search_fields = ('from_date', 'to_date')

class LimitAdmin(admin.ModelAdmin):
    list_display = ('user', 'year', 'initial', 'days_left', 'days_used')
    list_filter = ('user', 'year')
    sortable_by = ('user', 'year', 'days_initial')


# Register your models here.
admin.site.register(Absence, AbsenceAdmin)
admin.site.register(Limit, LimitAdmin)