from django.shortcuts import render, redirect
from .models import Patient, ClinicalData
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PatientListView(ListView):
    model=Patient

class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName', 'lastName', 'age')

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstName', 'lastName', 'age')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')

def addData(request, **kwargs):
    form=ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'MedicalApp/clinicaldata_form.html', {'form':form, 'patient':patient})

def analyzeData(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for entry in data:
        if entry.testName == 'hw':
            HeightAndWeight=entry.testName.split('/')
            if len(HeightAndWeight) > 1:
                feetToMetre = float(HeightAndWeight[0]) * 0.4536
                BMI = float(HeightAndWeight[1]/feetToMetre*2)
                bmiEntry = ClinicalData()
                bmiEntry.testName = 'BMI'
                bmiEntry.testValue = BMI
                responseData.append(bmiEntry)

        responseData.append(entry)
        print(responseData)

    return render(request, 'MedicalApp/testReport.html', {'data':responseData})

