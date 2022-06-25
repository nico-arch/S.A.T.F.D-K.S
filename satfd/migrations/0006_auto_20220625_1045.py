# Generated by Django 3.2.5 on 2022-06-25 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('satfd', '0005_auto_20220625_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gilet_couleur',
            options={'permissions': (('Gilet_couleur_voir', 'SATFD: voir'), ('Gilet_couleur_voir_inactif', 'SATFD: voir inactif'), ('Gilet_couleur_voir_details', 'SATFD: voir details'), ('Gilet_couleur_ajouter', 'SATFD: ajouter'), ('Gilet_couleur_modifier', 'SATFD: modifier'), ('Gilet_couleur_activer', 'SATFD: activer'), ('Gilet_couleur_desactiver', 'SATFD: desactiver'), ('Gilet_couleur_supprimer', 'SATFD: supprimer'))},
        ),
        migrations.AlterModelOptions(
            name='lieu_de_travail',
            options={'permissions': (('Station_lieu_de_travail_voir', 'SATFD: voir'), ('Station_lieu_de_travail_voir_inactif', 'SATFD: voir inactif'), ('Station_lieu_de_travail_voir_details', 'SATFD: voir details'), ('Station_lieu_de_travail_ajouter', 'SATFD: ajouter'), ('Station_lieu_de_travail_modifier', 'SATFD: modifier'), ('Station_lieu_de_travail_activer', 'SATFD: activer'), ('Station_lieu_de_travail_desactiver', 'SATFD: desactiver'), ('Station_lieu_de_travail_supprimer', 'SATFD: supprimer'))},
        ),
        migrations.AlterModelOptions(
            name='personne',
            options={'permissions': (('Personne_voir', 'SATFD: voir'), ('Personne_voir_inactif', 'SATFD: voir inactif'), ('Personne_voir_details', 'SATFD: voir details'), ('Personne_ajouter', 'SATFD: ajouter'), ('Personne_modifier', 'SATFD: modifier'), ('Personne_activer', 'SATFD: activer'), ('Personne_desactiver', 'SATFD: desactiver'), ('Personne_supprimer', 'SATFD: supprimer'))},
        ),
    ]
