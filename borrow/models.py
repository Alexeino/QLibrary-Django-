from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models.signals import pre_save, post_delete,post_save
# Create your models here.
def get_return_date():
    return datetime.today() + timedelta(days=20)

class BorrowedItem(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    borrow_person = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    return_date = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    is_delivered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.borrow_person.username} borrowed {self.book_id.title} " 
    
    

def add_return_date(sender,instance,*args,**kwargs):
    print("***************8Borrow Pre Save Model Recievers***************")
    borrowed_book = Book.objects.get(id = instance.book_id.id)
    print("Borrowed state reciever  -->",borrowed_book.is_borrowed)
    borrowed_book.is_borrowed = True
    borrowed_book.save()
    print("Borrowed Book is --> ",borrowed_book.title)
    print("Borrowed state reciever  -->",borrowed_book.is_borrowed)
    print("Return Date Function -->",get_return_date())
    if instance.return_date is None:
        print("Book Borrowed --> Adding Return Date...")
        instance.return_date = get_return_date()
        instance.save()
    elif instance.return_date is not None:
        print("Return Date Exists Already...........")
        pass
    print(instance.return_date)
    
        
post_save.connect(add_return_date,sender=BorrowedItem)

def change_borrow_state(sender,instance,*args,**kwargs):
    print("******************Change Borrow State Receiver***********")
    borrowed_book = Book.objects.get(id = instance.book_id.id)
    borrowed_book.is_borrowed = False
    borrowed_book.save()
    print(borrowed_book)
    
post_delete.connect(change_borrow_state,sender=BorrowedItem)