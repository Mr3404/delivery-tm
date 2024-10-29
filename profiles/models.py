from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user", related_name="user")
    firstname = models.CharField(max_length=20, verbose_name="First Name", blank=True, null=True)
    lastname = models.CharField(max_length=20, verbose_name="Last Name", blank=True, null=True)
    mobile = models.CharField(max_length=12, verbose_name="mobile phone", blank=True, null=True)


    class Meta:
        verbose_name_plural = "Profiles"

    
    def __str__(self) -> str:
        return str(self.firstname)
    
    @receiver(post_save, sender=User)
    def create_user_info(sender, instance, created, **kwargs):
        if created:
            profile = Profile(user=instance)
            profile.save()