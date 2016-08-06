from django import forms
from .models import reporte

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = reporte
        fields = '__all__'
         
 
