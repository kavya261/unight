# Generated by Django 4.0.6 on 2023-01-02 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_city_country_profile_skill_role_person_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skill_role',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
