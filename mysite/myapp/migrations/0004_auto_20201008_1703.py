# Generated by Django 3.1.2 on 2020-10-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201006_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestionmodel',
            name='image',
            field=models.ImageField(max_length=144, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='suggestionmodel',
            name='image_description',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
