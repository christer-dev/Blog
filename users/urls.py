from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from users.views import IndexView, LoginView, LogoutView, RegisterView, PasswordsChangeView, ProfileView, ModifyProfileView

app_name = 'users'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),

    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('modifyProfile/', ModifyProfileView.as_view(), name='modifyProfile'),
    path('password/', PasswordsChangeView.as_view(template_name='users/changePass.html'), name ='password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset', views.password_reset_request, name="password_reset"),
    path('logout/', LogoutView, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
'''path('createProfile/', CreateProfileView.as_view(), name='createProfile'),'''