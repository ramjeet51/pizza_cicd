# Generated by Django 4.2.4 on 2023-11-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
