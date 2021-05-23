from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)


class Leads(models.Model):
    first_name = models.CharField(_("first_name"), max_length=50)
    last_name = models.CharField(_("last_name"), max_length=50)
    age = models.IntegerField(_("age"), default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
