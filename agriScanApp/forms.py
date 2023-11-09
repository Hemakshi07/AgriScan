from django import forms
from .models import Membership, Courses, FilesStorage, CourseModules, Student, Quiz, Question, Answer
from .validators import validate_password, validate_username_length
from django.urls import reverse

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=(('Student', 'Student'), ('Professor', 'Professor')))

   
