from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=False)
    is_staff = models.BooleanField(default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'),
                                   verbose_name=_('Is Staff ?'))
    is_active = models.BooleanField(default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'),
                                    verbose_name=_('Is Active ?'))
    date_joined = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'name']

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    
    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return u'%s' % (self.name.strip())

    def get_short_name(self):
        return u'%s' % (self.name.strip())

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def show_name(self):
        """This name is used to show in site header"""
        allowed_length = 23
        name = self.get_full_name()
        if len(name) > allowed_length:
            name = name[:allowed_length] + "..."
        return name
