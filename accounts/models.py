from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse
# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'Site details/'
    ext = filename.split('.')[-1]

    if instance:
        filename = 'Logo.png'
    return os.path.join(upload_to, filename)

class main_app_details(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to=path_and_rename, default="[Original size] Smart Tech(1).png")

    def __str__(self):
        return self.name

class Site_Contacts(models.Model):
    site_name = models.ForeignKey(main_app_details, on_delete=models.CASCADE)
    site_status = models.BooleanField(default=True)
    site_number = models.PositiveSmallIntegerField(default=254202346703, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, default="smarttech.allservices@gmail.com")
    sms = models.PositiveSmallIntegerField(null=True, blank=True, default=254202346703)
    whatsapp = models.URLField(default="https://wa.me/c/254202346703", max_length=300, null=True,blank=True)
    facebook_page = models.URLField(default="https://fb.me/smarttech.all",max_length=300, null=True,blank=True)
    facebook_direct_message = models.URLField(default="https://m.me/smarttech.all", null=True,blank=True)
    twitter = models.URLField(default="https://twitter.com/Jeff18309725", null=True,blank=True)
    instagram = models.URLField(default="https://www.instagram.com/smarttech.allservices", null=True,blank=True)
    youtube = models.URLField(default="https://www.youtube.com/channel/UC4_F7e77uT7dG1EP99IdQow?sub_confirmation=1", null=True,blank=True)
    location = models.URLField(default="https://goo.gl/maps/jXQMRKzCB8h2hQcf6", null=True,blank=True)


def path_and_rename(instance, filename):
    upload_to = 'users_images/'
    ext = filename.split('.')[-1]

    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    profile_Pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", default="undraw_profile.svg")


    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    blogger = 'blogger'
    developer = 'developer'
    designer = 'designer'
    analyst = 'analyst'

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
        (blogger, 'blogger'),
        (developer, 'developer'),
        (designer, 'designer'),
        (analyst, 'analyst'),
    ]
    user_type = models.CharField(max_length=20, choices=user_types, default=student)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

class Subscribe(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, primary_key=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('index')