from django.contrib import admin

from .models import UserAccount

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['user','get_firstname','get_lastname','get_email','mobile']
    class Meta:
        model = UserAccount
        
    def get_firstname(self,obj):
        return obj.user.first_name
    
    def get_lastname(self,obj):
        return obj.user.last_name
    
    def get_email(self,obj):
        return obj.user.email
    

        
admin.site.register(UserAccount,UserAccountAdmin)