# Generated by Django 2.2.1 on 2019-08-08 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0041_delete_professor_duplicate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='prof_class',
        ),
        migrations.AddField(
            model_name='professor',
            name='prof_class',
            field=models.ManyToManyField(to='questions.OnlineClass'),
        ),
    ]
