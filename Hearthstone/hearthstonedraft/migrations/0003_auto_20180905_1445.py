# Generated by Django 2.1.1 on 2018-09-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hearthstonedraft', '0002_auto_20180905_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partie',
            name='date_heure_debut',
        ),
        migrations.RemoveField(
            model_name='partie',
            name='date_heure_modification',
        ),
    ]