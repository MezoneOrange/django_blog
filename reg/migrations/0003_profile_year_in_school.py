# Generated by Django 3.0.6 on 2020-05-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_profile_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]
