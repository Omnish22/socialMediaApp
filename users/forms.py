from django import forms 
from django.contrib.auth.models import User 
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    # TO CHANGE FIELD NAMES
    password = forms.CharField(label='Passoword', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = {'username', 'email', 'first_name', 'last_name'}

    def check_password(self):
        if self.cleaned_data['password']!=self.cleaned_data['password2']:
            raise forms.ValidationError('Password Not Match')
        return self.cleaned_data['passowrd2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = {'first_name','last_name','email'}

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'photo'}
