# Generated by Django 4.0.5 on 2022-06-26 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='post',
        ),
    ]
