from django import forms
from django.core.exceptions import ValidationError
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class story(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = (
            'heading',
            'content'
        )
    def clean_heading(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        return heading

