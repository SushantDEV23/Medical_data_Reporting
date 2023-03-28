from django.urls import path, include
from MedicalApp.api.views import PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('data', PatientViewSet, basename='names')

urlpatterns = [
    path('', include(router.urls))
]