from django import forms
from django.forms import ModelForm
from .models import VisitorsPost


class Post(ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class": "form-control","id": "title","placeholder": "Enter your message here..."}))
    content = forms.CharField(max_length=255, widget=forms.Textarea(attrs={"class":"form-control","id":"message","style":"height: 8rem", "placeholder":"Enter your message here..." }))

    class Meta:
        model = VisitorsPost
        fields = ['title', 'content']

