# Generated by Django 2.1.7 on 2019-03-28 20:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import registration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120)),
                ('age', models.IntegerField(default=25, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')], default='male', max_length=10)),
                ('phone_no', models.CharField(max_length=11)),
                ('image', models.ImageField(blank=True, null=True, upload_to=registration.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LogData',
            fields=[
                ('user', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.LogData'),
        ),
    ]