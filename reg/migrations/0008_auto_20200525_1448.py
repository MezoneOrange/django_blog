# Generated by Django 3.0.6 on 2020-05-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0007_auto_20200525_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='notice',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
