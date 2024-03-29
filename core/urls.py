"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', include('users.urls')),
    path('blogs/', include('blogs.urls')),
    path('users/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''path('success/', SuccessView.as_view(), name='success'),'''
'''
path('password/', PasswordsChangeView.as_view(template_name='users/changePass.html'), name ='password'),
path('reset/', PasswordsResetView.as_view(template_name='users/resetPass.html'), name ='reset'),
path('resetEmail/', PasswordsResetDoneView.as_view(), name ='resetDone'),
path('resetSet/', PasswordsResetConfirmView.as_view(), name ='resetSet'),
'''