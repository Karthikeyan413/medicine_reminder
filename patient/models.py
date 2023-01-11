from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserCredientials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.user.username


class PatientInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=20, null=False, blank=False)
    patient_age = models.PositiveIntegerField()
    patient_DOB = models.DateField()

    def __str__(self):
        return str(self.patient_name) + " " + str(self.patient_age) + " " + str(self.patient_DOB)


class MedicineInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=15, null=False, blank=False)
    medicine_type = models.CharField(max_length=10, null=False, blank=False)
    medicine_color = models.CharField(max_length=10, null=False, blank=False)
    problem = models.CharField(max_length=20, null=False, blank=False)
    medicine_quantity = models.PositiveIntegerField()
    medicine_intake = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class MedicineDT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user.username
