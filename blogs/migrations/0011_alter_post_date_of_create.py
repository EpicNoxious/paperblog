# Generated by Django 4.1.5 on 2023-02-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_alter_post_date_of_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
