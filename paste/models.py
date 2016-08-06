from django.db import models

# Create your models here.

class reporte (models.Model):
    cuerpo = models.TextField()
    fecha  = models.DateTimeField()
    # Yay
    
    
