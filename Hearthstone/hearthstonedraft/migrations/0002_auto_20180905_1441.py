# Generated by Django 2.1.1 on 2018-09-05 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hearthstonedraft', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partie',
            old_name='dateheure_debut',
            new_name='date_heure_debut',
        ),
        migrations.RenameField(
            model_name='partie',
            old_name='dateheure_modification',
            new_name='date_heure_modification',
        ),
        migrations.RenameField(
            model_name='partie',
            old_name='nom',
            new_name='nom_du_joueur',
        ),
    ]
