from django.contrib import admin
from .models import Doctor,patient,Appointment,patientDischargeDetails
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class patientAdmin(admin.ModelAdmin):
    pass
admin.site.register(patient, patientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class patientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(patientDischargeDetails, patientDischargeDetailsAdmin)
