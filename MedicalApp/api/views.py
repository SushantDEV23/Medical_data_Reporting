from MedicalApp.models import Patient
from MedicalApp.api.serializers import PatientSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]