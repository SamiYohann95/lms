# Generated by Django 5.0.6 on 2024-09-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
