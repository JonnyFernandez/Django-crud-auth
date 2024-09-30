from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "important"]
        # para darle estilos, bootstraps instalado
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "ingresa titulo"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "ingresa descripcion"}
            ),
            "important": forms.CheckboxInput(
                attrs={"class": "form-check-input text-center"}
            ),
        }
