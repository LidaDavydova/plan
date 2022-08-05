from doctest import Example
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TT = models.CharField(max_length=80, blank=True, null=True)
    example = models.CharField(max_length=80, blank=True, null=True)
    price = models.CharField(max_length=80, blank=True, null=True)
    mediakit = models.CharField(max_length=80, blank=True, null=True)
    AdRiver = models.CharField(max_length=20, blank=True, null=True)
    contacts = models.CharField(max_length=200, blank=True, null=True)
    launch = models.CharField(max_length=200, blank=True, null=True)
    seasons = models.CharField(max_length=200, blank=True, null=True)
    dop_comments = models.CharField(max_length=200, blank=True, null=True)
    prepayment = models.CharField(max_length=40, blank=True, null=True)
    budget = models.CharField(max_length=40, blank=True, null=True)
    minuses = models.CharField(max_length=200, blank=True, null=True)
    advantages = models.CharField(max_length=200, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()