# Generated by Django 3.1.2 on 2020-10-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20201009_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default_profile_photo.svg', upload_to='profile_image'),
        ),
    ]
