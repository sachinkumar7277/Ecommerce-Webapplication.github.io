from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile,Customer
@receiver(post_save,sender =User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance,name = instance.username)
        Customer.objects.create(user=instance, name=instance.username,email=instance.email)

