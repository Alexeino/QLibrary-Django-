from django.db import models
from django.db.models.signals import pre_save,post_save
from django.utils import timezone
from django.utils.text import slugify
from genres.models import Tag
from qlib.db.recievers import add_active_timestamp
from series.models import Series


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=220)
    author_id = models.CharField(max_length=220,null=True,blank=True)
    address = models.TextField()
    author_email = models.EmailField(verbose_name="Author's Email",blank=True,null=True)
    author_desc = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    series = models.ForeignKey(Series,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=220)
    tags = models.ManyToManyField(Tag,blank=True,null=True,related_name="book_tags")
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    short_desc = models.TextField()
    slug = models.SlugField(blank=True,null=True)
    book_id = models.CharField(max_length=220,unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    read_time_mins = models.IntegerField(blank=True,null=True)
    active_timestamp = models.DateTimeField(verbose_name="Last Activated",auto_now_add=False,null=True,blank=True)
    
    def __str__(self):
        return self.title
    

class BookProxy(Book):
    class Meta:
        proxy=True
        verbose_name = 'Active Book'
        verbose_name_plural = 'Active Books'

        
pre_save.connect(add_active_timestamp,sender=Book)

# Function to automatically assign book_id and slug
def add_book_id_slug(sender,instance,*args,**kwargs):
    title = instance.title
    
    if instance.slug is None:
        slug = instance.slug
        if slug is None:
            instance.slug = slugify(title)
    
    if instance.book_id is None:
        pure_title = ''.join(e for e in title if e.isalnum())
        print(pure_title)
        pure_author = ''.join(e for e in instance.author.name if e.isalnum())
        print(pure_author)
        booked_id = str(pure_author[0:4] + pure_title[0:4] + str(instance.pk))
        instance.book_id = booked_id.lower()
        
pre_save.connect(add_book_id_slug,sender=Book)

    