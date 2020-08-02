from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #model with which we want to work with here it is User model = database here
    class Meta:
        model = User # User is the table we created in database
        #in which order we want them to be in database and in display
        fields = ['username', 'email', 'password1', 'password2']

#update username or email here
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    # model with which we want to work with here it is User model = database here
    class Meta:
        model = User
        fields = ['username', 'email']

#update profile here
class ProfileUpadateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pimage']