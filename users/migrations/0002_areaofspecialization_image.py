# Generated by Django 3.2.9 on 2022-08-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaofspecialization',
            name='image',
            field=models.ImageField(default='empty.jpg', null=True, upload_to='images/', verbose_name='Profile picture'),
        ),
    ]
