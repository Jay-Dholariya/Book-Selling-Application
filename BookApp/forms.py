from django import forms 
from .models import Books2

class booksform(forms.ModelForm):
    content = forms.JSONField(required = False)
    title = forms.CharField(max_length=25)
    
    class Meta :
        model = Books2
        fields = '__all__'
