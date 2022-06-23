from django.db import models
from django.contrib.auth.models import User
from datetime import *
# from .form_models import *
import uuid
from django.utils import timezone
# Create your models here.


class Personne(models.Model):
    id = models.AutoField(primary_key = True)


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



class Station_lieu_de_travail(models.Model):
    id = models.AutoField(primary_key = True)



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
