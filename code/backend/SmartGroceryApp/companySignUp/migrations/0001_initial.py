# Generated by Django 3.2.7 on 2021-10-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('manager_name', models.CharField(max_length=80)),
                ('store_name', models.CharField(max_length=80)),
                ('store_location', models.CharField(max_length=80)),
                ('logo', models.ImageField(blank=True, default='company_logos/default_logo.png', null=True, upload_to='company_logos')),
                ('map_of_store', models.ImageField(blank=True, default='company_maps/default_map.png', null=True, upload_to='company_maps')),
            ],
            options={
                'db_table': 'company_info',
            },
        ),
    ]
