from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from random import randint
from django.utils.text import slugify
from qlib.db.recievers import add_active_timestamp
from genres.models import Genre
# Create your models here.
class Series(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    active_timestamp = models.DateTimeField(auto_now_add=False,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    series_id = models.CharField(max_length=220,null=True,blank=True)
    genre = models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True,blank=True)
    
    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "All Series"
    def __str__(self):
        return self.title
    
    @property
    def active(self):
        return self.is_active
      
pre_save.connect(add_active_timestamp,sender=Series)

# Function to automatically assign book_id and slug
def add_series_id_slug(sender,instance,*args,**kwargs):
    title = instance.title
    
    if instance.slug is None:
        slug = instance.slug
        if slug is None:
            instance.slug = slugify(title)
    
    if instance.series_id is None:
        pure_title = ''.join(e for e in title if e.isalnum())
        print(pure_title)
        # pure_author = ''.join(e for e in instance.author.name if e.isalnum())
        # print(pure_author)
        booked_id = str(pure_title[0:6] + str(randint(0,100000)))
        instance.series_id = booked_id.lower()
        
pre_save.connect(add_series_id_slug,sender=Series)

    