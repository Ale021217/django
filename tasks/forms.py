from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields=['titulo', 'descripcion', 'importancia']
        widgets= { 
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el titulo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe la descripcion'}),
            'importancia': forms.CheckboxInput(attrs={'class':'form-check-input text-center'})
        }
        