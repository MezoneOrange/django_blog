# Generated by Django 3.0.6 on 2020-05-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0005_profile_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='notice',
            field=models.BooleanField(default=True),
        ),
    ]
