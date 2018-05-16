from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Hotel, Rooms
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.layout import Layout, Submit, Div,Field,HTML,Fieldset, ButtonHolder

class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['room_type', 'price', 'number_available']
    def __init__(self,*args, **kwargs):
         super(RoomsForm, self).__init__(*args, **kwargs)
         self.helper = FormHelper()
         #self.helper.form_class = 'form-horizontal'
        #  self.helper.form_class = 'form-inline'
         self.helper.form_method = 'POST'
         self.helper.form_tag = True
         self.helper.layout = Layout(
         Div(
            Div(Field('room_type','number_available','price',css_class='form-control')),
            Div(
                ButtonHolder(
                Submit('Save', 'Add New Room', css_class='btn btn-primary'),
                HTML('<a class="btn btn-warning" href={% url "home" %}>Cancel</a>'),),css_class='col-md-12  submissons'
                )
            )
            )

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
