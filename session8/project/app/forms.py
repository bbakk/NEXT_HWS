from django import forms
from .models import POST

choices = [('HOBBY', 'HOBBY'), ('SECRET', 'SECRET'), ('CODING','CODING')]

class PostForm(forms.ModelForm):
    class Meta:
        model = POST
        fields = ('title', 'content', 'category')
    
    widget = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.TextInput(attrs={'class': 'form-control'}),
        'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
    }