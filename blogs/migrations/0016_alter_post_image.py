# Generated by Django 4.1.5 on 2023-02-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jepg', null=True, upload_to='images/'),
        ),
    ]