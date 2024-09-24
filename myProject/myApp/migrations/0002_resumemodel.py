# Generated by Django 5.0 on 2024-09-18 15:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_url', models.URLField(max_length=100, null=True)),
                ('github_url', models.URLField(max_length=100, null=True)),
                ('codepen_url', models.URLField(max_length=100, null=True)),
                ('yoursite_url', models.URLField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='Media/Pro_pic')),
                ('contact_no', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('skills_title', models.CharField(max_length=100, null=True)),
                ('education', models.CharField(max_length=100, null=True)),
                ('awards', models.CharField(max_length=100, null=True)),
                ('language', models.CharField(max_length=100, null=True)),
                ('Interest', models.CharField(max_length=100, null=True)),
                ('career_summery', models.TextField(max_length=100, null=True)),
                ('user', models.OneToOneField(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
