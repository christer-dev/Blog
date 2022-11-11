from pipes import Template
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .views import authenticate
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput)

    class Meta:
        model = get_user_model()
        fields = ['email']

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', required=True, max_length=150)
    password = forms.CharField(label='Password', widget =forms.PasswordInput())

    field = (
        'email',
        'password'
    )

    def auth(self, request):

        auth_email = self.cleaned_data.get('email')
        pword = self.cleaned_data.get('password')
        return authenticate(request, email=auth_email, password=pword)

'''class CreateProfileForm(forms.Form):
    first_name=forms.CharField(label='First Name')
    last_name=forms.CharField(label='Last Name')
    avatar = forms.ImageField(label='Profile Picture',widget=forms.FileInput)
    bio = forms.CharField(label='About Me',widget=forms.Textarea)
    
    class Meta:
        model = Profile
        
    field = (
        'first_name',
        'last_name',
        'avatar',
        'bio'
    )'''

class UpdateProfileForm(forms.ModelForm):
    first_name=forms.CharField(label='First Name')
    last_name=forms.CharField(label='Last Name')
    avatar = forms.ImageField(label='Profile Picture',widget=forms.FileInput)
    bio = forms.CharField(label='About Me',widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'bio']


'''class CreateProfileForm(forms.form):
    first_name = forms.CharField(label='first_name', required=True)
    last_name = forms.CharField(label='last_name', required=True)
    about_me = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField()'''


'''class CreateProfileForm(forms.Form):
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(max_length=250, required=True)
    birth_year = forms.DateField(widget=forms.SelectDateWidget())
    profile_image = forms.FileField()'''

'''class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')'''