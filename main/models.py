from djongo import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.forms import WordForm

class Words(models.Model):
    word = models.CharField(max_length=50)
    class Meta:
        abstract = True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=10)
    words = models.ArrayField(
        model_container = Words,
        model_form_class = WordForm,
        default = [],
    )
    objects = models.DjongoManager()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
