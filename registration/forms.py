from django import forms
from django.core.exceptions import ValidationError
from .models import 
from dal import autocomplete

User=get_user_model()

class profile_form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'fullname','gender','age','phone_no','image'
        )
    
