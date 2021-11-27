from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # email, first_name, last_name, username, setpassword() done
    mobile = models.CharField(max_length=14,null=True,blank=True)
    # otp for Future Otp Authentication
    has_book = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.first_name    

def create_user_account(instance,sender,created,*args,**kwargs):
    
    if created:
        account = UserAccount.objects.create(user = instance)
    
    else:
        pass

post_save.connect(create_user_account,sender=User)