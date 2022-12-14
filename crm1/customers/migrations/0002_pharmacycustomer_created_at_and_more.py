# Generated by Django 4.0.6 on 2022-08-20 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacycustomer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pharmacycustomer',
            name='created_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_created_pharmacy_customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pharmacycustomer',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pharmacycustomer',
            name='edited_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_edited_pharmacy_customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
