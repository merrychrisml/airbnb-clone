# Generated by Django 2.2.5 on 2021-05-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210507_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]
