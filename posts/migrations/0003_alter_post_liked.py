# Generated by Django 3.2.4 on 2021-07-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_follows'),
        ('posts', '0002_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(related_name='liked_by', to='users.Profile'),
        ),
    ]
