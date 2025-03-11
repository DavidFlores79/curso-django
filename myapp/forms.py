from django import forms
from .models import Project


class CreateNewTask(forms.Form):
    title = forms.CharField(
        label="Title", 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=200,
        required=True
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}), 
        label="Description"
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class':'form-control'}),
        label="Project"
    )
    
class CreateNewProject(forms.Form):
    name = forms.CharField(
        label="Name", 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=200,
        required=True
    )
