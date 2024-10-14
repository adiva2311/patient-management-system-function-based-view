from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    patient_name        = models.CharField(max_length=255)

    GENDER_CHOICES = [
        ("Laki-laki" , "Laki-laki"),
        ("Perempuan" , "Perempuan"),
    ]

    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES)
    born_date   = models.DateField()
    visit_date  = models.DateTimeField(auto_now_add=True, blank=True)
    symptom     = models.TextField()
    slug        = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.patient_name)
        super(Patient, self).save()

    def __str__(self):
        return '{}. {}'.format (self.id, self.patient_name)

    
