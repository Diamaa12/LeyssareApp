# Generated by Django 4.1.4 on 2023-03-11 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BleyApp', '0006_mamadounotes_samednotes_delete_myuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MamadouNotes',
        ),
        migrations.DeleteModel(
            name='SamedNotes',
        ),
    ]
