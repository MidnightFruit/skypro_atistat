# Generated by Django 5.1.3 on 2024-12-03 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetworkManager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contry',
            new_name='country',
        ),
    ]
