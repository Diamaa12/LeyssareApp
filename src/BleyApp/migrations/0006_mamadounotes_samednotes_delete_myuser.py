# Generated by Django 4.1.4 on 2023-03-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BleyApp', '0005_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MamadouNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SamedNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
