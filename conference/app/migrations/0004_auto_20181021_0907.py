# Generated by Django 2.1.2 on 2018-10-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181021_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
