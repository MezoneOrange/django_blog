# Generated by Django 3.0.6 on 2020-05-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='notice',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
