from django.forms import ModelForm
from .models import Ciius
class CrearForm(ModelForm):
    class Meta:
        model = Ciius
        fields = ['codigo','actividad']