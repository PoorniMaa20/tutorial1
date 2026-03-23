from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.patient)