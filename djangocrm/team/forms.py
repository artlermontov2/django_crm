from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import UserModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'})
    )
    username = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})
    )
    password1 = forms.CharField(
        label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
    )
    password2 = forms.CharField(
        label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password confirmation'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddUserForm(forms.ModelForm):
    email = forms.EmailField(
        label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'})
    )
    first_name = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'*First_name'})
    )
    last_name = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'*Last_name'})
    )  
    phone = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'8-000-000-00-00'})
    ) 
        
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'phone', 'email']

    
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})
    )
    password = forms.CharField(
        label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
    )
    class Meta:
        model = User
        fields = ['username', 'password']


