# Generated by Django 5.0.3 on 2024-03-14 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profil',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.city'),
        ),
        migrations.AddField(
            model_name='profil',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.country'),
        ),
    ]