from django import forms
from django.forms import ModelForm

from photo.models import Profile


class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')