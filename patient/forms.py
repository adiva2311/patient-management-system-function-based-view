from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_name', 'gender', 'born_date', 'symptom']
        labels = {
            'patient_name' : 'Nama Pasien',
            'gender' : 'Jenis Kelamin',
            'born_date' : 'Tanggal Lahir',
            'symptom' : 'Gejala yang Dialami Pasien'
        }

        widget = {
            'patient_name' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'gender' : forms.RadioSelect(attrs = {'class' : 'form-check'}),
            'born_date' : forms.DateInput(attrs = {'class' : 'form-control'}),
            'symptom' : forms.Textarea(attrs = {'class' : 'form-control'}),
        }