from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']  # ENLEVER 'created_at' ICI
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la tâche'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description...'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
