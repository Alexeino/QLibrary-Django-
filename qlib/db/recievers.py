from django.utils import timezone

# Function to assign activation timestamp to the book once its activated.
def add_active_timestamp(sender,instance,*args,**kwargs):
    is_active = instance.is_active
    # print("status  ",is_active)
    if is_active and instance.active_timestamp is None:
        instance.active_timestamp = timezone.now()
    elif not is_active and instance.active_timestamp is not None:
        instance.active_timestamp = None