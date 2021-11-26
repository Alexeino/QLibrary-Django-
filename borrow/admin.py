from django.contrib import admin

from borrow.models import BorrowedItem

# Register your models here.
class BorrowedItemAdmin(admin.ModelAdmin):
    list_display=['book_id','borrow_person','return_date','is_delivered']
    class Meta:
        model = BorrowedItem
        
admin.site.register(BorrowedItem,BorrowedItemAdmin)