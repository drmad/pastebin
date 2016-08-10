from django.db import models

# Create your models here.

class reporte (models.Model):
    cuerpo = models.TextField()
    fecha  = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=5)

    # Yay
    def __str__(self):
    	#codigo = hashlib.md5(str(self.id)).hexdigest()[:5]
    	
    	return str(self.cuerpo[0:10])





    
