# Generated by Django 3.2.5 on 2022-06-25 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satfd', '0004_personne_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gilet_couleur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('couleur', models.CharField(max_length=254, null=True, unique=True)),
                ('date_created', models.DateField(blank=True, default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=500, null=True)),
                ('date_modified', models.DateField(null=True)),
                ('modified_by', models.CharField(max_length=500, null=True)),
            ],
            options={
                'permissions': (('Gilet_couleur_voir', 'Paco: voir'), ('Gilet_couleur_voir_inactif', 'Paco: voir inactif'), ('Gilet_couleur_voir_details', 'Paco: voir details'), ('Gilet_couleur_ajouter', 'Paco: ajouter'), ('Gilet_couleur_modifier', 'Paco: modifier'), ('Gilet_couleur_activer', 'Paco: activer'), ('Gilet_couleur_desactiver', 'Paco: desactiver'), ('Gilet_couleur_supprimer', 'Paco: supprimer')),
            },
        ),
        migrations.AddField(
            model_name='personne',
            name='sexe',
            field=models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], max_length=50, null=True, verbose_name='Sexe'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='mere_cin_nif',
            field=models.CharField(default='', max_length=254, null=True, verbose_name='CIN/NIF de la mère'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='pere_cin_nif',
            field=models.CharField(default='', max_length=254, null=True, verbose_name='CIN/NIF du père'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='gilet_couleur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='satfd.gilet_couleur'),
        ),
    ]
