# Generated by Django 4.2.5 on 2023-11-13 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Quota',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
