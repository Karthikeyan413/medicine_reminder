from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from patient.forms import RegisterForm, RegisterNoForm, PatientInfoForm, MedicalInfoForm, MedicalDTForm
from patient.models import UserCredientials, PatientInfo, MedicineDT, MedicineInfo
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.cache import never_cache
# import datetime as dt
# import time
# import smtplib

# Create your views here.


@csrf_protect
def register_user(request):
    if(request.user.is_authenticated):
        logout(request)
    registered = False
    if request.method == 'POST':
        form_register = RegisterForm(data=request.POST)
        form_registerNo = RegisterNoForm(data=request.POST)

        if form_register.is_valid() and form_registerNo.is_valid():
            user = form_register.save()
            user.set_password(user.password)
            user.save()

            regno = form_registerNo.save(commit=False)
            regno.user = user
            regno.save()

            registered = True

        else:
            print(form_register.errors, form_registerNo.errors)
    else:
        form_register = RegisterForm()
        form_registerNo = RegisterNoForm()
    if(registered):
        return HttpResponseRedirect('/medicare/login')
    else:
        return render(request, 'login/register.html', {
                                                'form_register': form_register,
                                                'form_registerNo': form_registerNo,
                                                 })


@csrf_protect
def user_login(request):
    if(request.user.is_authenticated):
        logout(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        user = authenticate(username=username, password=password)

        if user:
            if(user.is_active):
                login(request, user)
                return HttpResponseRedirect('/medicare/index')

            else:
                return HttpResponse("Account Not Active")
        else:
            # print("u={}p={}".format(username, password))
            return render(request, 'login/login.html', {'invaliduser': True})
    else:
        return render(request, 'login/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/medicare/login')


@csrf_protect
@login_required
def delete_user(request):
    # logout(request)
    if request.user.is_superuser:
        print("Not permitted")
        return HttpResponse("Superuser can not be deleted")
    try:
        # print(User.objects.get(username=request.user.username))
        user = User.objects.get(username=request.user.username)
        user.delete()
        return HttpResponseRedirect('/medicare/register')
    except User.DoesNotExist:  # Not sure
        return HttpResponseRedirect('/medicare/register')
    except:
        print("Some other error")
        return HttpResponseRedirect('/medicare/register')


@login_required
@csrf_protect
def index(request):
    if(PatientInfo.objects.filter(user_id=request.user.id).exists()):
        return HttpResponseRedirect('/medicare/index2')

    if request.method == 'POST':
        form_patient_info = PatientInfoForm(data=request.POST)
        form_medical_info = MedicalInfoForm(data=request.POST)
        form_medical_dt = MedicalDTForm(data=request.POST)

        if form_patient_info.is_valid() and form_medical_dt.is_valid() and form_medical_info.is_valid():

            patient = form_patient_info.save(commit=False)
            # print(User.objects.get(username=request.user))
            patient.user = User.objects.get(username=request.user)

            medicalinfo = form_medical_info.save(commit=False)
            medicalinfo.user = User.objects.get(username=request.user)

            medicaldt = form_medical_dt.save(commit=False)
            medicaldt.user = User.objects.get(username=request.user)

            medicaldt.save()
            medicalinfo.save()
            patient.save()

            return HttpResponseRedirect('/medicare/index2')
        else:
          print(form_patient_info.errors,
                form_medical_dt.errors, form_medical_info.errors)
    else:
        form_patient_info = PatientInfoForm()
        form_medical_dt = MedicalDTForm()
        form_medical_info = MedicalInfoForm()

    return render(request, 'main/index.html', {
                                                'form_patient_info': form_patient_info,
                                                'form_medical_dt': form_medical_dt,
                                                'form_medical_info': form_medical_info,
                                                })


@csrf_protect
@login_required
def index2(request):
    try:
        patientinfo = PatientInfo.objects.get(user_id=request.user.id)
        medicineinfo = MedicineInfo.objects.get(user_id=request.user.id)
        medicine_dt = MedicineDT.objects.get(user_id=request.user.id)

        patient = str(patientinfo)
        patient = patient.split()

        # def send_email():
        #     email_user = 'karthick.as413@gmail.com'
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.starttls()
        #     server.login(email_user, 'eytjdvfyikxhjojm')
        #     to_user = request.user.mail
        #     #EMAIL
        #     message = 'sending this from python!'
        #     server.sendmail(email_user, to_user, message)
        #     server.quit()
        #
        # def send_email_at(send_time):
        #     time.sleep(send_time.timestamp() - time.time())
        #     send_email()
        #     print('email sent')

        # # set your sending time in UTC
        # first_email_time = dt.datetime(2022, 2, 27, 9, 0, 0)
        # # set the interval for sending the email
        # interval = dt.timedelta(minutes=24*60)
        #
        # send_time = first_email_time
        # while True:
        #     send_email_at(send_time)
        #     send_time = send_time + interval
    except:
        return HttpResponse("Patient Information Not Found!")

    if request.method == 'POST':
        try:
            patientinfo.delete()
            medicineinfo.delete()
            medicine_dt.delete()
        except:
            return HttpResponse("Record doesn't exists")
        return HttpResponseRedirect('/medicare/index')
    return render(request, 'main/index2.html', {
                                                'name': patient[0],
                                                'age': patient[1],
                                                'DOB': patient[2],
                                                })
