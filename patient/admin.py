from django.contrib import admin
from .models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'visit_date']

admin.site.register(Patient,PatientAdmin)