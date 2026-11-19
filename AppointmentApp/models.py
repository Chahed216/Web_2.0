from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=true)
    updated_at = models.DateTimeField(auto_now=true)
    appointment_date = models.DateTimeField()
    