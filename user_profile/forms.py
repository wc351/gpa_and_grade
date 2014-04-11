from django import forms
from user_profile.models import User_Profile


class AddUserForm(forms.ModelForm):
     class Meta:
         model = User_Profile
         fields = ('username', 'year_level', 'lat', 'lon', 'school')
