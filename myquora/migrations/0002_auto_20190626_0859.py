# Generated by Django 2.2.2 on 2019-06-26 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='username',
            new_name='user',
        ),
    ]
