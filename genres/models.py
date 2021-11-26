from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
from qlib.db.recievers import add_active_timestamp

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=220)
    slug = models.SlugField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    active_timestamp = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
       
pre_save.connect(add_active_timestamp,sender=Genre)

def add_genre_slug(sender,instance,*args,**kwargs):
    title = instance.title
    
    if instance.slug is None:
        slug = instance.slug
        if slug is None:
            instance.slug = slugify(title)
            
pre_save.connect(add_genre_slug,sender=Genre)

class Tag(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(unique=True,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.title