# Generated by Django 4.1.5 on 2023-02-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_remove_post_author_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='./'),
        ),
    ]
