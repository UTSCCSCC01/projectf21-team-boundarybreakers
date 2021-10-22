# Generated by Django 3.2.8 on 2021-10-22 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyInventory', '0002_remove_companyinventory_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinventory',
            name='aisle',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyinventory',
            name='shelf',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
