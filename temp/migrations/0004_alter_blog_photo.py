# Generated by Django 4.0 on 2021-12-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0003_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(upload_to='static/photos'),
        ),
    ]