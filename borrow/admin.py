from django.contrib import admin

from borrow.models import BorrowedItem
from books.models import Book

# Register your models here.
class BorrowedItemAdmin(admin.ModelAdmin):
    list_display=['book_id','get_borrow_person','return_date','is_delivered','is_returned','book_returned_date']
    readonly_fields = ['book_returned_date','return_date']
    class Meta:
        model = BorrowedItem
    
    def get_borrow_person(self,obj):
        return obj.borrow_person.user.username
    
    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name == "book_id" and not "change" in request.path : #simple hack to not filter book if i am updating or deleting book.
            kwargs["queryset"] = Book.objects.filter(is_borrowed = False)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)
        
admin.site.register(BorrowedItem,BorrowedItemAdmin)