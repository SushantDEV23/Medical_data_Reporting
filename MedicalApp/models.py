from django.db import models

class Patient(models.Model):
    lastName=models.CharField(max_length=20)
    firstName=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.firstName +' '+ self.lastName

class ClinicalData(models.Model):
    TEST_NAMES=[('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    testName=models.CharField(choices=TEST_NAMES, max_length=20)
    testValue=models.CharField(max_length=20)
    testDate=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)