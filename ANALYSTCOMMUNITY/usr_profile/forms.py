from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User= get_user_model()

from .models import Profile
from django.forms.models import ModelForm

from django.forms.widgets import FileInput

class ProfileFrom(ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'
        exclude=['user']
        widgets={
            'user_profile_image': FileInput(),
        }