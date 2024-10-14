from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Patient
from .forms import PatientForm

# Create your views here.
def index(request):
    patients = Patient.objects.all()
    context = {
        'page_title':'Patient List',
        'heading':'Data Pasien',
        'patients':patients,
    }
    return render(request, 'patient/index.html', context)

def patient_detail(request, id):
    patient = Patient.objects.get(pk=id)
    return render(request, 'patient/index.html', {'patient':patient})

# def add(request):
#     if request.method == 'POST':
#         Patient.objects.create(
#             patient_name = request.POST['patient_name'],
#             gender = request.POST['gender'],
#             born_date = request.POST['born_date'],
#             symptom = request.POST['symptom'],
#         )

def add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST or None)
        if form.is_valid():
            new_patient_name = form.cleaned_data['patient_name']
            new_gender = form.cleaned_data['gender']
            new_born_date = form.cleaned_data['born_date']
            new_symptom = form.cleaned_data['symptom']

            new_patient = Patient(
                patient_name = new_patient_name,
                gender = new_gender,
                born_date = new_born_date,
                symptom = new_symptom,
            )
            new_patient.save()
            return render(request, 'patient/add_patient.html', {
                'form':PatientForm(),
                'success':True
                }
            )
    else:
        form = PatientForm()
    return render(request, 'patient/add_patient.html', {'form':PatientForm()})

def edit(request, id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=id)
        form = PatientForm(request.POST or None, instance=patient)
        if form.is_valid():
            form.save()
            return render(request, 'patient/edit_patient.html', {
                'form':form,
                'success':True
                })
    else:
        patient = Patient.objects.get(pk=id)
        form = PatientForm(instance=patient)
    return render(request, 'patient/edit_patient.html', {
                'form':form,
                })

def delete(request, id):
    if request.method == 'POST':
        patient = Patient.objects.get(pk=id)
        patient.delete()
    return redirect('patient:index')
        