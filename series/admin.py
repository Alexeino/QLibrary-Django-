from django.contrib import admin
from django.db import models

from books.models import Book
from .models import Series

# Register your models here.

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    read_only = ['title']
    fields = ['title','order','author','is_active']

class SeriesAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ['title','id','is_active']
    class Meta:
        model = Series
admin.site.register(Series,SeriesAdmin)

