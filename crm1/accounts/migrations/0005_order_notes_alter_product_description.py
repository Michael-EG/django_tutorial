# Generated by Django 4.0.6 on 2022-07-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
