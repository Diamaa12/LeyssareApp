# Generated by Django 4.1.4 on 2023-01-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BleyApp', '0003_rename_montant_cfa_leyssaredepenses_montant_depensee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leyssaremembres',
            name='id_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
