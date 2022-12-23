from django import forms
from django.contrib.auth.forms import UserCreationForm


class VisitorsPost(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))


