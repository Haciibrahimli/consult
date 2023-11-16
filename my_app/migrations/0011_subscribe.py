# Generated by Django 4.2.7 on 2023-11-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_remove_sosialmedia_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
            options={
                'verbose_name': 'abune',
                'verbose_name_plural': 'abuneler',
                'ordering': ('-created_at',),
            },
        ),
    ]
