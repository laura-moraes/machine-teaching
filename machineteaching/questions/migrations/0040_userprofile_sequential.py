# Generated by Django 2.2.1 on 2019-08-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0039_auto_20190808_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='sequential',
            field=models.BooleanField(default=True),
        ),
    ]
