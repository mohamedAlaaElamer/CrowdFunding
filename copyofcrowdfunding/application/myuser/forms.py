from django import forms
from django.forms import ModelForm, widgets
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class RegisterationForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'
        widgets={
            'First_Name' : forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Name' : forms.TextInput(attrs={'class': 'form-control'}),
            'Email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'Password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'Confirm_Password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'Phone_Number' : PhoneNumberPrefixWidget(attrs={'class': 'form-control mt-2 mb-2'}, initial = 'EG'),
            'Profile_Picture' : forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
        }

        def clean(self):
            cleaned_data = super(RegisterationForm, self).clean()
            password = cleaned_data.get("Password")
            confirm_password = cleaned_data.get("Confirm_Password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['Email', 'Password']
        

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'
        exclude = ('Email',)
        widgets={
            'First_Name' : forms.TextInput(attrs={'class': 'form-control'}),
            'Last_Name' : forms.TextInput(attrs={'class': 'form-control'}),
            'Password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'Confirm_Password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'Phone_Number' : PhoneNumberPrefixWidget(attrs={'class': 'form-control mt-2 mb-2'}, initial = 'EG'),
            'Profile_Picture' : forms.ClearableFileInput(attrs={'class': 'form-control mt-2'})
        }

        def clean(self):
            cleaned_data = super(RegisterationForm, self).clean()
            password = cleaned_data.get("Password")
            confirm_password = cleaned_data.get("Confirm_Password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )        