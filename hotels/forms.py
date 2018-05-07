from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Hotel, Rooms


class RoomsForm(forms.ModelForm):
    room_type = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Room Type eg.Delux"}))
    number_available = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'eg.10'}))

    class Meta:
        model = Rooms
        fields = ['room_type', 'price', 'number_available']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
