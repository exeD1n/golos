from .models import All
from django import forms
from django.forms import TextInput, EmailInput, Select

class AllForm(forms.ModelForm):
    
    class Meta:
        model = All
        fields = ('fullName', 'mail', 'formOfStudy', 'group', 'courseOfStudy', 'hilary_id')
        
        widgets = {
            'fullName': TextInput(attrs={
                'class' : 'form-control mb-3',
                'placeholder' : 'ФИО'
            }),
            
            'mail': EmailInput(attrs={
                'class' : 'form-control mb-3',
                'placeholder' : 'name@gmail.com'
            }),
            
            'formOfStudy' : Select(attrs={
                'class' : 'form-control mb-3',
            }),
            
            'group' : Select(attrs={
                'class' : 'form-control mb-3',
            }),
            
            'courseOfStudy' : Select(attrs={
                'class' : 'form-control mb-3',
            }),
            
            'hilary_id' : Select(attrs={
                'class' : 'form-control mb-3',
            }),
        }

        
        
