from django.contrib import admin

from borrow.models import BorrowedItem
from books.models import Book

# Register your models here.
class BorrowedItemAdmin(admin.ModelAdmin):
    list_display=['book_id','borrow_person','return_date','is_delivered']
    class Meta:
        model = BorrowedItem
        
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name == "book_id" and not "change" in request.path : #simple hack to not filter book if i am updating or deleting book.
            kwargs["queryset"] = Book.objects.filter(is_borrowed = False)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)
        
admin.site.register(BorrowedItem,BorrowedItemAdmin)