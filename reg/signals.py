from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
    """Creates new unit in Profile table when creates new unit in User table, and linking these units."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwards):
    """Refreshes unit when it was refreshed."""
    instance.profile.save()
