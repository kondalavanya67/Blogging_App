# Generated by Django 2.1.7 on 2019-04-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/cover_photos/'),
        ),
    ]
