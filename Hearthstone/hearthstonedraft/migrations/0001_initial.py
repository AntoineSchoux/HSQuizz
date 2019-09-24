# Generated by Django 2.1.1 on 2018-09-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateheure_debut', models.DateTimeField(auto_now_add=True)),
                ('dateheure_modification', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
    ]
