from django.contrib import admin
from patient.models import UserCredientials, PatientInfo, MedicineInfo, MedicineDT
# Register your models here.
admin.site.register(UserCredientials)
admin.site.register(PatientInfo)
admin.site.register(MedicineInfo)
admin.site.register(MedicineDT)
