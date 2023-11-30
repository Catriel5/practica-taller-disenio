
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import  Evento

class InicioSesionForm(AuthenticationForm):
    pass



class RegistroEventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre_evento', 'descripcion_evento', 'fecha_evento', 'lugar_evento', 'presupuesto_evento']
        

class FormularioInscripcion(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    telefono = forms.CharField(label='Teléfono', max_length=15)
    lugar_procedencia = forms.CharField(label='Lugar de procedencia', max_length=30)
    fecha_llegada = forms.DateField(label='Fecha de llegada', widget=forms.DateInput(attrs={'type': 'date'}))
