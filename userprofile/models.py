from django.db import models
from django.contrib.auth import get_user_model
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Adresses(models.Model):
    street_adress = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    postal_code = models.CharField(max_length=225)
    phone = PhoneField(help_text="Contact Number")

    def __str__(self):
        return self.street_adress


User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_adress = models.ManyToManyField(Adresses)


    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


