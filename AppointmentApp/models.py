from django.db import models
from AccountApp.models import Doctor Patient

# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        blanke=True,
        upload_to='presciptions/',
    )
    class status(models.TextField):
        PENDING = "PENDING","en attente"
        CONFIRMED = "CONFIRMED", "confirmé"
        CANCELLED = "CANCELLED", "annulé"
        status = models.CharField(max_length=10,choices=status.choice,default=status.PENDING)
        status = models.CharField(max_length=10,choices=status.choice,default=status.PENDING)
        duration_minutes = models.PositiveIntegerField( default = 30)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        appointment_date = models.DateTimeField()
        Doctor = models.ForeignKey("Doctor",on_delete=models.CASCADE,related_name="appointments")
        ##patient = models.ForeignKey(AccountApp.) 
        Patient = models.ForeignKey("Patient",on_delete=models.CASCADE,related_name="appointments")