# Generated by Django 3.1.1 on 2020-10-29 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='breed_name',
            new_name='name',
        ),
    ]
