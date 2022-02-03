from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

from .managers import CustomUserManager


# Create your models here.


class Client(AbstractUser):
    STATUS_CHOICES = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('external', 'External'),
        ('indirect', 'Indirect')
    ]
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown')
    ]
    phone_number = models.CharField(max_length=255, verbose_name='Phone number', unique=True)
    additional_numbers = ArrayField(models.CharField(max_length=255), verbose_name='Additional phone numbers',
                                    blank=True, null=True)
    first_name = models.CharField(max_length=150, verbose_name='First name of Client', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Last name of Client', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    # check
    status_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    status = models.CharField(max_length=255, verbose_name='Status', choices=STATUS_CHOICES, blank=True, null=True)
    type = models.CharField(max_length=255, verbose_name='Type', blank=True, null=True)
    email = ArrayField(models.EmailField(max_length=255), verbose_name='E-mail(s) of Client', blank=True, null=True)
    sex = models.CharField(max_length=255, choices=SEX_CHOICES, verbose_name='Sex', blank=True, null=True)
    timezone = models.CharField(max_length=255, verbose_name='Timezone', blank=True, null=True)
    vk = ArrayField(models.CharField(max_length=255), verbose_name='Vkontakte', blank=True, null=True)
    fb = ArrayField(models.CharField(max_length=255), verbose_name='Facebook', blank=True, null=True)
    ok = models.CharField(max_length=255, verbose_name='Odnoklassniki', blank=True, null=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', blank=True, null=True)
    telegram = models.CharField(max_length=255, verbose_name='Telegram', blank=True, null=True)
    whatsapp = models.CharField(max_length=255, verbose_name='Whatsapp', blank=True, null=True)
    viber = models.CharField(max_length=255, verbose_name='Viber', blank=True, null=True)

    username = None
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.id:
            last = self.__class__.objects.last()
            if not last:
                last_id = 1
            else:
                last_id = last.id
            self.id = (last_id // 100 + 1) * 100 + 1
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the username of client
        """
        return f"{self.phone_number} - {self.first_name} {self.last_name}"

    class Meta(AbstractUser.Meta):
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        swappable = 'AUTH_USER_MODEL'


class Entity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_title = models.CharField(max_length=255, verbose_name='Full title')
    short_title = models.CharField(max_length=255, verbose_name='Short title')
    tin = models.PositiveBigIntegerField(verbose_name='Taxpayer Identification Number')
    reason_code = models.PositiveSmallIntegerField(verbose_name='Reason of code')

    def save(self, *args, **kwargs):
        if not self.id:
            last = self.__class__.objects.last()
            if not last:
                last_id = 1
            else:
                last_id = last.id
            self.id = (last_id // 100 + 1) * 100 + 2
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    def __str__(self):
        """Return full title of Entity"""
        return self.full_title


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name of Departments')
    # check
    department = models.ForeignKey('self', verbose_name='Department', related_name='child', on_delete=models.CASCADE,
                                   blank=True, null=True)
    entity = models.ForeignKey(Entity, verbose_name='Entity', related_name='departments', on_delete=models.CASCADE)
    client = models.ManyToManyField(Client, verbose_name='Clients', related_name='clients')

    def save(self, *args, **kwargs):
        if not self.id:
            last = self.__class__.objects.last()
            if not last:
                last_id = 1
            else:
                last_id = last.id
            self.id = (last_id // 100 + 1) * 100 + 3
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Return full title of Department"""
        return self.name
