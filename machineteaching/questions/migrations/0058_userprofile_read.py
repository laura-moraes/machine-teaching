# Generated by Django 2.2.5 on 2020-08-29 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0057_auto_20200805_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
