# Generated by Django 2.1.1 on 2018-10-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj_base', '0005_new_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='last_updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
