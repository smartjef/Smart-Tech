from django import forms
from django.contrib.auth.models import User
from accounts.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()
    fields = (
        'username', 'first_name', 'last_name', 'email'
    )

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    blogger = 'blogger'
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_types = [
        (student, 'student'),
        (parent, 'parent'),
        (blogger, 'blogger'),
    ]
    user_type = forms.ChoiceField(choices=user_types, required=True)

    class Meta():
        model = user_profile
        fields = ('bio', 'profile_Pic', 'user_type')
