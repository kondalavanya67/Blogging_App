from django import forms
from django.core.exceptions import ValidationError
from .models import Blog, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class story(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Blog
        fields = (
            'heading',
        )
    def clean_heading(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        return heading

class comment(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 2}))
    class Meta:
        model = Comment
        fields=(
        'content',
        )
