# Generated by Django 3.2.8 on 2024-09-22 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_intermediate_languagemodel_languagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='intermediate_experienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_experience_name', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='experienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_name', models.CharField(max_length=10, null=True)),
                ('proficiency_level', models.CharField(choices=[('high', 'High'), ('low', 'Low'), ('medium', 'Medium')], max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'experience_name')},
            },
        ),
    ]
