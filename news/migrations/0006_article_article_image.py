# Generated by Django 3.0 on 2019-12-13 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='articles/'),
        ),
    ]
