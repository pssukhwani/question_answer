# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-07 20:17
from __future__ import unicode_literals

import core.models.user_profile
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created',
                 django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified',
                 django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('answer', models.TextField()),
                ('accepted_or_not', models.BooleanField(default=False, help_text=b'User can accept the answer')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, help_text=b'Location of user', max_length=225, null=True)),
                ('title',
                 models.CharField(help_text=b"Title/Headline that describes user's specialities", max_length=100)),
                ('description', models.TextField(verbose_name=b'Tell us something about yourself')),
                ('personal_website',
                 models.CharField(blank=True, help_text=b'Personal website/portfoliolink', max_length=225, null=True)),
                ('twitter_username',
                 models.CharField(blank=True, help_text=b'Twitter username', max_length=100, null=True)),
                ('github_username',
                 models.CharField(blank=True, help_text=b'Github username', max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, help_text=b"User's profile pic", null=True,
                                             upload_to=core.models.user_profile.get_upload_path)),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created',
                 django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified',
                 django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=225)),
                ('question', models.TextField(verbose_name=b'Question')),
                ('rating', models.IntegerField(default=0, verbose_name=b'Up-vote/Down-vote')),
                ('reputation', models.IntegerField(default=0, verbose_name=b'Reputation')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'Name of the tag', max_length=200, verbose_name=b'Tag Name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'name',
                                                                   unique=True)),
            ],
        ),
    ]
