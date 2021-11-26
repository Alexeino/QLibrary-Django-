from django.contrib import admin
from django.db import models
from .models import Book,Author,BookProxy

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','id','author_id','author_email']
    class Meta:
        model = Author

admin.site.register(Author,AuthorAdmin)
    
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id','id','title','author']
    class Meta:
        model = Book
admin.site.register(Book,BookAdmin)

class BookProxyAdmin(admin.ModelAdmin):
    list_display = ['book_id','id','title','author','is_active','active_timestamp']
    search_fields = ['title']
    list_filter = ['is_active']
    
    class Meta:
        model = BookProxy
        
    def get_queryset(self,request):
        return BookProxy.objects.filter(is_active = True)
    
admin.site.register(BookProxy,BookProxyAdmin)