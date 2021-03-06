from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from time import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_supersuer, **extra_fields):
        '''
        Creates and saves a User with the given email and password
        '''
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_supersuer=is_supersuer, last_login=now, date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True, null=True)
    first_name = models.CharField(max_length=254, blank=True)
    second_name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(blank=True, unique=True)
    address1 = models.CharField(max_length=254, blank=True)
    address2 = models.CharField(max_length=254, blank=True)
    area_code = models.CharField(max_length=20, blank=True)
    country_code = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address1', 'address2', 'area_code', 'country_code']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def ged_absolute_url(self):
        return '/users/%s/' % urlquote(self.email)

    def get_full_name(self):
        """:return: first_name plus the last_name, with space in between"""
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        """:return short name for user"""
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """sends email to this user"""
        send_mail(subject, message, from_email, [self.email])