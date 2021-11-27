from django.db import models
from accounts.models import UserAccount
from books.models import Book
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db.models.signals import pre_save, post_delete,post_save
# Create your models here.
def get_return_date():
    return datetime.today() + timedelta(days=20)

class BorrowedItem(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    borrow_person = models.ForeignKey(UserAccount,on_delete=models.SET_NULL,null=True)
    return_date = models.DateTimeField(auto_now_add=False,null=True,blank=True)
    is_delivered = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    book_returned_date = models.DateField(auto_now_add=False,blank=True,null=True)
    
    def __str__(self):
        return f"{self.borrow_person.user.username} borrowed {self.book_id.title} " 
    
    
def add_book_returned_date(sender,instance,*args,**kwargs):
    print("***********Book returned reciever, Saving date to the Transaction********")
    borrowed_book = Book.objects.get(id = instance.book_id.id)
    borrow_person = UserAccount.objects.get(id = instance.borrow_person.id)
    if instance.is_returned == True:
        instance.book_returned_date = datetime.today()
        instance.is_delivered = False
        borrowed_book.is_borrowed = False
        borrow_person.has_book = False
        borrow_person.save()
        borrowed_book.save()
        print("Book Returned, Transaction Date Saved...")
    else:
        pass
    print("Return method on ",borrowed_book)
    

def add_return_date(sender,instance,*args,**kwargs):
    print("***************8Borrow Pre Save Model Recievers***************")
    borrowed_book = Book.objects.get(id = instance.book_id.id)
    borrow_person = UserAccount.objects.get(id = instance.borrow_person.id)
    print(borrow_person)
    # print("Borrowed state reciever  -->",borrowed_book.is_borrowed)
    borrowed_book.is_borrowed = True
    borrow_person.has_book = True
    borrow_person.save()
    borrowed_book.save()
    # print("Borrowed Book is --> ",borrowed_book.title)
    # print("Borrowed state reciever  -->",borrowed_book.is_borrowed)
    # print("Return Date Function -->",get_return_date())
    if instance.return_date is None:
        # print("Book Borrowed --> Adding Return Date...")
        instance.return_date = get_return_date()
        instance.save()
    elif instance.return_date is not None:
        # print("Return Date Exists Already...........")
        pass
    print(instance.return_date)
    
        
pre_save.connect(add_return_date,sender=BorrowedItem)
pre_save.connect(add_book_returned_date,sender=BorrowedItem)

def change_borrow_state(sender,instance,*args,**kwargs):
    print("******************Change Borrow State Receiver***********")
    borrowed_book = Book.objects.get(id = instance.book_id.id)
    borrowed_book.is_borrowed = False
    borrowed_book.save()
    print(borrowed_book)
    
post_delete.connect(change_borrow_state,sender=BorrowedItem)