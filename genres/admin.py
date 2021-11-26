from django.contrib import admin

from .models import Genre, Tag

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title','id','slug','is_active','active_timestamp']
    search_fields = ['title']
    list_filter = ['is_active']
    class Meta:
        model = Genre
        
        
admin.site.register(Genre,GenreAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model=Tag
admin.site.register(Tag,TagAdmin)