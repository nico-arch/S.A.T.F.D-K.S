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

class Gilet_couleur(models.Model):
    id = models.AutoField(primary_key = True)
    couleur = models.CharField(max_length=254, unique=True, null =True)


    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        permissions = ( ("Gilet_couleur_voir", "SATFD: voir"),
                        ("Gilet_couleur_voir_inactif", "SATFD: voir inactif"),
                        ("Gilet_couleur_voir_details", "SATFD: voir details"),
                        ("Gilet_couleur_ajouter", "SATFD: ajouter"),
                        ("Gilet_couleur_modifier", "SATFD: modifier"),
                        ("Gilet_couleur_activer", "SATFD: activer"),
                        ("Gilet_couleur_desactiver", "SATFD: desactiver"),
                        ("Gilet_couleur_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format(self.couleur)

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
        permissions = ( ("Station_lieu_de_travail_voir", "SATFD: voir"),
                        ("Station_lieu_de_travail_voir_inactif", "SATFD: voir inactif"),
                        ("Station_lieu_de_travail_voir_details", "SATFD: voir details"),
                        ("Station_lieu_de_travail_ajouter", "SATFD: ajouter"),
                        ("Station_lieu_de_travail_modifier", "SATFD: modifier"),
                        ("Station_lieu_de_travail_activer", "SATFD: activer"),
                        ("Station_lieu_de_travail_desactiver", "SATFD: desactiver"),
                        ("Station_lieu_de_travail_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format(self.nom)

class Personne(models.Model):
    class Meta:
        ordering = ('date_created',)

    id = models.AutoField(primary_key = True)
    prenom = models.CharField(max_length=254,  null =True)
    nom = models.CharField(max_length=254,  null =True)

    naissance = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    sexe = models.CharField('Sexe',
                                   max_length=50,
                                   choices=sexe_Type,
                                   null=True)
    adresse = models.CharField(max_length=254,  null =True)
    telephone = models.CharField('Numéro de téléphone',max_length=254, unique=True, default ='', null =True)
    email = models.CharField('Email',max_length=254, unique=True, default ='', null =True)
    lieu_de_travail = models.ForeignKey( Lieu_de_travail ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    id_number = models.CharField('NIU',max_length=254, unique=True, default ='', null =True)
    id_plaque = models.CharField('Numéro de plaques',max_length=254, unique=True, default ='', null =True)
    gilet_couleur = models.ForeignKey( Gilet_couleur ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    # qty_enfants = models.IntegerField ('Quantité d'enfants',null=True)
    conjoint = models.CharField('NIU du/de la conjoint(e)',max_length=254, unique=True, default ='', null =True)

    pere_cin_nif = models.CharField('NIU du père',max_length=254, default ='', null =True)
    mere_cin_nif = models.CharField('NIU de la mère',max_length=254, default ='', null =True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        permissions = ( ("Personne_voir", "SATFD: voir"),
                        ("Personne_voir_inactif", "SATFD: voir inactif"),
                        ("Personne_voir_details", "SATFD: voir details"),
                        ("Personne_ajouter", "SATFD: ajouter"),
                        ("Personne_modifier", "SATFD: modifier"),
                        ("Personne_activer", "SATFD: activer"),
                        ("Personne_desactiver", "SATFD: desactiver"),
                        ("Personne_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format((self.prenom+' '+self.nom+' '+self.id_number))
