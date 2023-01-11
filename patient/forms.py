from django import forms
from django.contrib.auth.models import User
from django.core import validators
from patient.models import UserCredientials, PatientInfo, MedicineInfo, MedicineDT


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Username',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'user@mail.com',
        }
    ))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control input',
        }
    ))

    class Meta():
        model = User
        fields = ['username', 'password', 'email']


class RegisterNoForm(forms.ModelForm):
    phone_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Phone Number',
        }
    ))

    class Meta():
        model = UserCredientials
        fields = ('phone_no',)


class PatientInfoForm(forms.ModelForm):
    patient_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Patient Name',
        }
    ))
    patient_age = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Patient Age',
        }
    ))
    patient_DOB = forms.DateField(required=True, widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control',
        }
    ))

    class Meta():
        model = PatientInfo
        fields = ('patient_name', 'patient_age', 'patient_DOB')


class MedicalInfoForm(forms.ModelForm):
    type_choices = (('Tablet', 'Tablet'), ('Capsule', 'Capsule'),
                    ('Drops', 'Drops'), ('Inhaler', 'Inhaler'), ('Injection', 'Injection'))
    color_choices = (('White', 'White'), ('Red', 'Red'), ('Yellow', 'Yellow'), ('Blue', 'Blue'), ('Green', 'Green'),
                     ('Orange', 'Orange'), ('Purple', 'Purple'), ('Brown', 'Brown'), ('Pink', 'Pink'), ('Grey', 'Gray'))
    medicine_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Medicine name',
        }
    ))
    medicine_type = forms.ChoiceField(choices=type_choices)
    medicine_type.widget.attrs.update({'class': 'form-select'})
    medicine_color = forms.ChoiceField(choices=color_choices)
    medicine_color.widget.attrs.update({'class': 'form-select'})
    problem = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Problem',
        }
    ))
    medicine_quantity = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'amount of medicine to be taken',
        }
    ))
    medicine_intake = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'number of dose per day',
        }
    ))

    class Meta():
        model = MedicineInfo
        fields = ('medicine_name', 'medicine_type', 'medicine_color',
                  'problem', 'medicine_quantity', 'medicine_intake')


class MedicalDTForm(forms.ModelForm):
    time = forms.TimeField(required=True, widget=forms.TimeInput(
        attrs={
            'type': 'time',
            'class': 'form-control',
        }
    ))
    start_date = forms.DateField(required=True, widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control',
        }
    ))
    end_date = forms.DateField(required=True, widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'form-control',
        }
    ))

    class Meta():
        model = MedicineDT
        fields = ('time', 'start_date', 'end_date')
