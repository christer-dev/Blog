from multiprocessing import AuthenticationError
from urllib import request
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm

from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.contrib.auth.decorators import login_required 

from django.contrib.auth import login, logout, authenticate
from django.views.generic.base import TemplateView, View
from django.urls import reverse_lazy

from django.contrib import messages

from .forms import LoginForm, RegisterForm, UpdateProfileForm
from .models import CustomUser, Profile
from blogs.models import Post


#testview
class IndexView(TemplateView):
    template_name = 'users/index.html'

    def get(self, request):
        return render(request, self.template_name)


class ProfileView(TemplateView):
    template_name='users/profile.html'

    #gets posts of user logged in and profile details of user
    def get(self, request):
        posts = Post.objects.filter(authorEmail=request.user)
        profile = Profile.objects.get(id=request.user.id)
        context = {
            'posts' : posts,
            'profile' : profile
        }
        return render(request, self.template_name, context)


class ModifyProfileView(TemplateView):
    template_name='users/modifyProfile.html'

    def get(self, request):
        form = UpdateProfileForm()
        return render(request, 'users/modifyProfile.html', {'form' : form})
    
    def post(self, request):
        #get profile of user currently logged in
        profileUser = Profile.objects.get(id=request.user.id)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profileUser)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile has been updated successfully!')
            return redirect('users:profile')

        else:
            profile_form = UpdateProfileForm(request.user.profile)
    
        return render(request, 'users/modifyProfile.html', {'profile_form' : profile_form})


class LoginView(TemplateView):

    template_name = 'users/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request,'users/login.html', {'form' : form})

    def post(self, request):
        form = LoginForm(request.POST)

        #import pdb; pdb.set_trace()

        if form.is_valid():
            
            #passes email and pass, and authenticates it
            username = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Successfuly Logged In!')
                return HttpResponseRedirect(reverse_lazy('blogs:index'))
            else:
                form = LoginForm(request.POST)
                return render(request, 'users/login.html', {'form' : form})
        
        else:
            return render(request, 'users/login.html', {'form': form})


def LogoutView(request):
    logout(request)
    return redirect('blogs:index')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = CustomUser.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "users/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset/done/") 
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})

#gets a passwordchange template from django
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')


class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password2'])
            user.save()     
            email = request.POST['email']
            password = request.POST['password2']

            user = authenticate(request, email=email, password=password)   
            return redirect('blogs:index')

        else:
            form = RegisterForm(request.POST)
            return render(request, 'users/register.html', {'form' : form})






'''class IndexView(TemplateView):
    template_name = 'users/index.html'
    
    def get(self, request):
        #import pdb; pdb.set_trace()
        last_name = CustomUser.last_name
        first_name = CustomUser.first_name
        context = {
            'last_name' : last_name,
            'first_name' : first_name
        }
        return render(request, self.template_name, context)'''





# Create your views here.
