from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Employee


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'age', 'salary', 'email', 'address', 'phone', 'profile_image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter age'}),
            'salary': forms.NumberInput(attrs={'placeholder': 'Enter salary'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address', 'rows': 3}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone'}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter current password'})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'})
    )
