# Generated by Django 4.0.6 on 2022-08-20 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_receipt_reference', models.CharField(default='', max_length=100)),
                ('external_issue_date', models.DateTimeField()),
                ('customer_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.pharmacycustomer')),
            ],
        ),
    ]