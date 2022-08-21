# Generated by Django 4.0.6 on 2022-08-20 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_rename_name_en_pharmacycustomer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_number', models.CharField(default='', max_length=20)),
                ('floor_number', models.CharField(default='', max_length=20)),
                ('building_number', models.CharField(default='', max_length=20)),
                ('street_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(default='مرسى مطروح', max_length=100)),
                ('country', models.CharField(default='مصر', max_length=50)),
                ('customer_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.pharmacycustomer')),
            ],
        ),
    ]
