# Generated by Django 4.0.5 on 2022-06-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogpost_owner_comment_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=1000)),
            ],
        ),
    ]
