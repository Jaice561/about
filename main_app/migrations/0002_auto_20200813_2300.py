# Generated by Django 3.0.5 on 2020-08-13 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img_src',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
