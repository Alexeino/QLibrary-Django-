from django.contrib import admin

from .models import Genre

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title','id','slug','is_active','active_timestamp']
    class Meta:
        model = Genre
        
        
admin.site.register(Genre,GenreAdmin)