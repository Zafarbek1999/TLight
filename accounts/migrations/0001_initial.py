# Generated by Django 3.2 on 2022-01-31 17:10

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=255, unique=True, verbose_name='Phone number')),
                ('additional_numbers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='Additional phone numbers')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='First name of Client')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Last name of Client')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status_updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('primary', 'Primary'), ('secondary', 'Secondary'), ('external', 'External'), ('indirect', 'Indirect')], max_length=255, null=True, verbose_name='Status')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Type')),
                ('email', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=255), blank=True, null=True, size=None, verbose_name='E-mail(s) of Client')),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('unknown', 'Unknown')], max_length=255, null=True, verbose_name='Sex')),
                ('timezone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Timezone')),
                ('vk', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='Vkontakte')),
                ('fb', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='Facebook')),
                ('ok', models.CharField(blank=True, max_length=255, null=True, verbose_name='Odnoklassniki')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Instagram')),
                ('telegram', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telegram')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Whatsapp')),
                ('viber', models.CharField(blank=True, max_length=255, null=True, verbose_name='Viber')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_title', models.CharField(max_length=255, verbose_name='Full title')),
                ('short_title', models.CharField(max_length=255, verbose_name='Short title')),
                ('tin', models.PositiveBigIntegerField(verbose_name='Taxpayer Identification Number')),
                ('reason_code', models.PositiveSmallIntegerField(verbose_name='Reason of code')),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name of Departments')),
                ('client', models.ManyToManyField(related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='Clients')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='accounts.entity', verbose_name='Entity')),
            ],
        ),
    ]
