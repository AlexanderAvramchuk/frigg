# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(User):
    """User with app settings."""
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    phone_number = PhoneNumberField(null=True)


    # Use UserManager to get the create_user method, etc.
    objects = UserManager()





def create_custom_user(sender, instance, created, **kwargs):
    if created:
        values = {}
        for field in sender._meta.local_fields:
            values[field.attname] = getattr(instance, field.attname)
        user = CustomUser(**values)
        user.save()

post_save.connect(create_custom_user, User)