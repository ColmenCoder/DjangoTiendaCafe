from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nomApe','email','direccion','password1','password2']

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    motivo = forms.ChoiceField(choices=[('sugerencia', 'Sugerencia'), ('queja', 'Queja'), ('otro', 'Otro')])
    mensaje = forms.CharField(widget=forms.Textarea)