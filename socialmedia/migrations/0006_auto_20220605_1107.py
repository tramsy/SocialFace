# Generated by Django 3.2.7 on 2022-06-05 05:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialmedia', '0005_followerscount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FollowersCount',
            new_name='FollowingCount',
        ),
        migrations.RenameField(
            model_name='followingcount',
            old_name='followers',
            new_name='following_user_name',
        ),
    ]
