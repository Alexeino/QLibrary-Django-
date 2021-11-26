from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.utils.text import slugify
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
        
        
# Function to assign activation timestamp to the book once its activated.
def add_active_timestamp(sender,instance,*args,**kwargs):
    is_active = instance.is_active
    # print("status  ",is_active)
    if is_active and instance.active_timestamp is None:
        instance.active_timestamp = timezone.now()
    elif not is_active and instance.active_timestamp is not None:
        instance.active_timestamp = None
        
pre_save.connect(add_active_timestamp,sender=Genre)

def add_genre_slug(sender,instance,*args,**kwargs):
    title = instance.title
    
    if instance.slug is None:
        slug = instance.slug
        if slug is None:
            instance.slug = slugify(title)
            
pre_save.connect(add_genre_slug,sender=Genre)
