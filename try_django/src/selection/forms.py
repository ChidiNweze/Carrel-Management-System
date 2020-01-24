from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Carrel, Floor
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': 'Your 8-character UWaterloo username',
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'student_ID',
            'Program',
            'gender']

class SelectForm(forms.ModelForm):
    class Meta:
        post = forms.MultipleChoiceField()
        model = Student
        fields = ['floor', 'Carrel']
        

