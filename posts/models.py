from __future__ import unicode_literals 
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True,blank=True,width_field="width_field",height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id":self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Gallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=False,blank=False,width_field="width_field",height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    #video = models.FileField(upload_to="videos/",null=True,blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery_detail", kwargs={"id":self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Program(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True,blank=True,width_field="width_field",height_field="height_field")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    #video = models.FileField(upload_to="videos/",null=True,blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("program_detail", kwargs={"id":self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Contact_us(models.Model):
    contact_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(null=False,blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-updated"]

class Registration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)    
    date_of_birth = models.DateField(max_length=20, blank=False, null=False)
    address = models.TextField(null=False,blank=False)
    contact_number = models.IntegerField()
    hieght = models.IntegerField()
    email = models.EmailField()
    education = models.CharField(max_length=120)
    employment = models.CharField(max_length=120)
    about_you = models.TextField(null=False,blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "-updated"]







