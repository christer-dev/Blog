from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.contrib import admin
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

'''class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)'''


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    # first_name = models.CharField(max_length=250)
    # last_name = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True,default='defaultAvatar.png', upload_to='profile_images')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    bio = models.TextField()

    def __str__(self):
        return self.user.email

'''
    @receiver(post_save, sender=CustomUser)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=CustomUser)
    def save_profile(sender,instance, **kwargs):
        instance.profile.save()'''


'''class Profile(models.model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    about_me = models.TextField()
    picture = models.ImageField(upload_to='Profile Picture')'''
# Create your models here.
