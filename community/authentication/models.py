from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,PermissionsMixin
        )
# Create your models here.

from .manager import UserManager

class User(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,unique=True)

    is_admin = models.BooleanField(default=False)

    id_superuser = models.BooleanField(default=False)

    id_staff = models.BooleanField(default=False)

    id_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name ='user'
        verbose_name_plural = 'users'
    def get_userid(self):
        return User.objects.get(username=self.username).user_id

