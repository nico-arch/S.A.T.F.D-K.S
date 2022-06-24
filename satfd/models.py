from django.db import models
from django.contrib.auth.models import User
from datetime import *
# from .form_models import *
import uuid
from django.utils import timezone
# Create your models here.



sexe_Type = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme'),
    # ('Autre', 'Autre'),
)


class Lieu_de_travail(models.Model):
    id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length=254, unique=True, null =True)


    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        permissions = ( ("Station_lieu_de_travail_voir", "Paco: voir"),
                        ("Station_lieu_de_travail_voir_inactif", "Paco: voir inactif"),
                        ("Station_lieu_de_travail_voir_details", "Paco: voir details"),
                        ("Station_lieu_de_travail_ajouter", "Paco: ajouter"),
                        ("Station_lieu_de_travail_modifier", "Paco: modifier"),
                        ("Station_lieu_de_travail_activer", "Paco: activer"),
                        ("Station_lieu_de_travail_desactiver", "Paco: desactiver"),
                        ("Station_lieu_de_travail_supprimer", "Paco: supprimer"),
        )

    def __str__(self):
        return '{0}'.format(self.user)

class Personne(models.Model):
    id = models.AutoField(primary_key = True)
    Prenom = models.CharField(max_length=254,  null =True)
    nom = models.CharField(max_length=254,  null =True)

    naissance = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    adresse = models.CharField(max_length=254,  null =True)
    telephone = models.CharField('Numéro de téléphone',max_length=254, unique=True, default ='', null =True)
    lieu_de_travail = models.ForeignKey( Lieu_de_travail ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    id_number = models.CharField('CIN/NIF',max_length=254, unique=True, default ='', null =True)
    id_plaque = models.CharField('Numéro de plaques',max_length=254, unique=True, default ='', null =True)
    gilet_couleur = models.CharField('Couleur de Gilet',max_length=254, unique=True, default ='', null =True)
    # qty_enfants = models.IntegerField ('Quantité d'enfants',null=True)
    conjoint = models.CharField('CIN/NIF du/de la conjoint(e)',max_length=254, unique=True, default ='', null =True)

    pere_cin_nif = models.CharField('CIN/NIF du père',max_length=254, unique=True, default ='', null =True)
    mere_cin_nif = models.CharField('CIN/NIF de la mère',max_length=254, unique=True, default ='', null =True)
    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        permissions = ( ("Personne_voir", "Paco: voir"),
                        ("Personne_voir_inactif", "Paco: voir inactif"),
                        ("Personne_voir_details", "Paco: voir details"),
                        ("Personne_ajouter", "Paco: ajouter"),
                        ("Personne_modifier", "Paco: modifier"),
                        ("Personne_activer", "Paco: activer"),
                        ("Personne_desactiver", "Paco: desactiver"),
                        ("Personne_supprimer", "Paco: supprimer"),
        )

    def __str__(self):
        return '{0}'.format(self.user)
