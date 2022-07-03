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
statut_demande = (
    ('En cours', 'En cours'),
    ('Approuvé', 'Approuvé'),
    ('Rejeté', 'Rejeté'),
    ('Visualisé', 'Visualisé'),
)
statut_personne = (
    ('Vivant','Vivant'),
    ('Malade','Malade'),
    ('Mort','Mort'),
)
#Section Surcursale#############################################################
class Surcursale(models.Model):
    id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length=254, unique=True, null =True)
    adresse = models.CharField(max_length=254, unique=True, null =True)
    montant_caisse = models.FloatField(null=True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Surcursale_voir", "SATFD: voir"),
                        ("Surcursale_voir_inactif", "SATFD: voir inactif"),
                        ("Surcursale_voir_details", "SATFD: voir details"),
                        ("Surcursale_ajouter", "SATFD: ajouter"),
                        ("Surcursale_modifier", "SATFD: modifier"),
                        ("Surcursale_activer", "SATFD: activer"),
                        ("Surcursale_desactiver", "SATFD: desactiver"),
                        ("Surcursale_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.nom+" Montant de la caisse: "+self.montant_caisse)
#Section Employé################################################################
class Employe(models.Model):
    id = models.AutoField(primary_key = True)
    utilisateur = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                help_text='', null =True)
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
    id_number = models.CharField('NIU',max_length=254, unique=True, default ='', null =True)
    surcursale = models.ForeignKey( Surcursale ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    salaire = models.FloatField(null=True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Employe_voir", "SATFD: voir"),
                        ("Employe_voir_inactif", "SATFD: voir inactif"),
                        ("Employe_voir_details", "SATFD: voir details"),
                        ("Employe_ajouter", "SATFD: ajouter"),
                        ("Employe_modifier", "SATFD: modifier"),
                        ("Employe_activer", "SATFD: activer"),
                        ("Employe_desactiver", "SATFD: desactiver"),
                        ("Employe_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format((self.prenom+' '+self.nom+' '+self.id_number))

#Section des personnes inscrites################################################
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
        ordering = ('date_created',)
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
        ordering = ('date_created',)
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
    id = models.AutoField(primary_key = True)

    utilisateur = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                help_text='', null =True)

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
    statut = models.CharField('Statut',
                                   max_length=50,
                                   choices=statut_personne,
                                   null=True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
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

#Section Source monétaire externe###############################################
class Src_mone_ext(models.Model):
    id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length=254, unique=True, null =True)
    adresse = models.CharField(max_length=254, unique=True, null =True)
    remarque = models.CharField(max_length=254, unique=True, null =True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Src_mone_ext_voir", "SATFD: voir"),
                        ("Src_mone_ext_voir_inactif", "SATFD: voir inactif"),
                        ("Src_mone_ext_voir_details", "SATFD: voir details"),
                        ("Src_mone_ext_ajouter", "SATFD: ajouter"),
                        ("Src_mone_ext_modifier", "SATFD: modifier"),
                        ("Src_mone_ext_activer", "SATFD: activer"),
                        ("Src_mone_ext_desactiver", "SATFD: desactiver"),
                        ("Src_mone_ext_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.nom+" Adresse: "+self.adresse)

#Section demande de renflouement################################################
class Dmd_renfl_ext(models.Model):
    id = models.AutoField(primary_key = True)
    montant = models.FloatField(null=True)
    sucursale_source = models.ForeignKey( Surcursale ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    source_monetaire_cible = models.ForeignKey( Src_mone_ext ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    employé = models.ForeignKey( Employe ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    statut_demande = models.CharField('Statut',
                                   max_length=50,
                                   choices=statut_demande,
                                   null=True)


    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Dmd_renfl_ext_voir", "SATFD: voir"),
                        ("Dmd_renfl_ext_voir_inactif", "SATFD: voir inactif"),
                        ("Dmd_renfl_ext_voir_details", "SATFD: voir details"),
                        ("Dmd_renfl_ext_ajouter", "SATFD: ajouter"),
                        ("Dmd_renfl_ext_modifier", "SATFD: modifier"),
                        ("Dmd_renfl_ext_activer", "SATFD: activer"),
                        ("Dmd_renfl_ext_desactiver", "SATFD: desactiver"),
                        ("Dmd_renfl_ext_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("source: "+self.sucursale_source+" cible: "+self.source_monetaire_cible+"Montant: "+self.montant)
class Dmd_renfl_int(models.Model):
    id = models.AutoField(primary_key = True)
    montant = models.FloatField(null=True)
    sucursale_source = models.ForeignKey( Surcursale , related_name='sucursale_source',
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    sucursale_cible = models.ForeignKey( Surcursale , related_name='sucursale_cible',
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    employé = models.ForeignKey( Employe ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    statut_demande = models.CharField('Statut',
                                   max_length=50,
                                   choices=statut_demande,
                                   null=True)


    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Dmd_renfl_int_voir", "SATFD: voir"),
                        ("Dmd_renfl_int_voir_inactif", "SATFD: voir inactif"),
                        ("Dmd_renfl_int_voir_details", "SATFD: voir details"),
                        ("Dmd_renfl_int_ajouter", "SATFD: ajouter"),
                        ("Dmd_renfl_int_modifier", "SATFD: modifier"),
                        ("Dmd_renfl_int_activer", "SATFD: activer"),
                        ("Dmd_renfl_int_desactiver", "SATFD: desactiver"),
                        ("Dmd_renfl_int_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("source: "+self.sucursale_source+" cible: "+self.sucursale_cible+"Montant: "+self.montant)

#Section paiment################################################################
class Paiements_hebdo(models.Model):
    id = models.AutoField(primary_key = True)
    personne_inscrite = models.ForeignKey( Personne ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    employé = models.ForeignKey( Employe ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    montant = models.FloatField(null=True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Paiements_hebdo_voir", "SATFD: voir"),
                        ("Paiements_hebdo_voir_inactif", "SATFD: voir inactif"),
                        ("Paiements_hebdovoir_details", "SATFD: voir details"),
                        ("Paiements_hebdo_ajouter", "SATFD: ajouter"),
                        ("Paiements_hebdo_modifier", "SATFD: modifier"),
                        ("Paiements_hebdo_activer", "SATFD: activer"),
                        ("Paiements_hebdo_desactiver", "SATFD: desactiver"),
                        ("Paiements_hebdo_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.personne_inscrite+" Montant: "+self.montant+"Date: "+self.date_created)
class Paiements_dettes(models.Model):
    id = models.AutoField(primary_key = True)
    personne_inscrite = models.ForeignKey( Personne ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    employé = models.ForeignKey( Employe ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    montant = models.FloatField(null=True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Paiements_dettes_voir", "SATFD: voir"),
                        ("Paiements_dettes_voir_inactif", "SATFD: voir inactif"),
                        ("Paiements_dettes_voir_details", "SATFD: voir details"),
                        ("Paiements_dettes_ajouter", "SATFD: ajouter"),
                        ("Paiements_dettes_modifier", "SATFD: modifier"),
                        ("Paiements_dettes_activer", "SATFD: activer"),
                        ("Paiements_dettes_desactiver", "SATFD: desactiver"),
                        ("Paiements_dettes_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.personne_inscrite+" Montant: "+self.montant+"Date: "+self.date_created)

#Section Prets##################################################################
class Prets(models.Model):
    id = models.AutoField(primary_key = True)
    personne_inscrite = models.ForeignKey( Personne ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    employé = models.ForeignKey( Employe ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    montant = models.FloatField(null=True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Prets_voir", "SATFD: voir"),
                        ("Prets_voir_inactif", "SATFD: voir inactif"),
                        ("Prets_voir_details", "SATFD: voir details"),
                        ("Prets_ajouter", "SATFD: ajouter"),
                        ("Prets_modifier", "SATFD: modifier"),
                        ("Prets_activer", "SATFD: activer"),
                        ("Prets_desactiver", "SATFD: desactiver"),
                        ("Prets_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.personne_inscrite+" Montant: "+self.montant+"Date: "+self.date_created)

#Section Employé mortuaire######################################################
class Morgue(models.Model):
    id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length=254, unique=True, null =True)
    adresse = models.CharField(max_length=254, unique=True, null =True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Morgue_voir", "SATFD: voir"),
                        ("Morgue_voir_inactif", "SATFD: voir inactif"),
                        ("Morgue_voir_details", "SATFD: voir details"),
                        ("Morgue_ajouter", "SATFD: ajouter"),
                        ("Morgue_modifier", "SATFD: modifier"),
                        ("Morgue_activer", "SATFD: activer"),
                        ("Morgue_desactiver", "SATFD: desactiver"),
                        ("Morgue_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.nom+" Montant de la caisse: "+self.montant_caisse)

class Employe_mortuaire(models.Model):
    id = models.AutoField(primary_key = True)
    utilisateur = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                help_text='', null =True)
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
    id_number = models.CharField('NIU',max_length=254, unique=True, default ='', null =True)
    morgue = models.ForeignKey( Morgue ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)


    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Employe_mortuaire_voir", "SATFD: voir"),
                        ("Employe_mortuaire_voir_inactif", "SATFD: voir inactif"),
                        ("Employe_mortuaire_voir_details", "SATFD: voir details"),
                        ("Employe_mortuaire_ajouter", "SATFD: ajouter"),
                        ("Employe_mortuaire_modifier", "SATFD: modifier"),
                        ("Employe_mortuaire_activer", "SATFD: activer"),
                        ("Employe_mortuaire_desactiver", "SATFD: desactiver"),
                        ("Employe_mortuaire_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format((self.prenom+' '+self.nom+' '+self.id_number))
class Rapport_deces(models.Model):
    id = models.AutoField(primary_key = True)
    personne_inscrite = models.ForeignKey( Personne ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    employé = models.ForeignKey( Employe_mortuaire ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    montant = models.FloatField(null=True)
    date = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,

                              )
    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Rapport_deces_voir", "SATFD: voir"),
                        ("Rapport_deces_voir_inactif", "SATFD: voir inactif"),
                        ("Rapport_deces_voir_details", "SATFD: voir details"),
                        ("Rapport_deces_ajouter", "SATFD: ajouter"),
                        ("Rapport_deces_modifier", "SATFD: modifier"),
                        ("Rapport_deces_activer", "SATFD: activer"),
                        ("Rapport_deces_desactiver", "SATFD: desactiver"),
                        ("Rapport_deces_supprimer", "SATFD: supprimer"),
        )
    def __str__(self):
        return '{0}'.format("Nom: "+self.personne_inscrite+" Montant: "+self.montant+"Date: "+self.date_created)
#Section Employé mortuaire######################################################
class Hopital(models.Model):
    id = models.AutoField(primary_key = True)
    nom = models.CharField(max_length=254, unique=True, null =True)
    adresse = models.CharField(max_length=254, unique=True, null =True)

    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Hopital_voir", "SATFD: voir"),
                        ("Hopital_voir_inactif", "SATFD: voir inactif"),
                        ("Hopital_voir_details", "SATFD: voir details"),
                        ("Hopital_ajouter", "SATFD: ajouter"),
                        ("Hopital_modifier", "SATFD: modifier"),
                        ("Hopital_activer", "SATFD: activer"),
                        ("Hopital_desactiver", "SATFD: desactiver"),
                        ("Hopital_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format("Nom: "+self.nom+" Montant de la caisse: "+self.montant_caisse)

class Medecin(models.Model):
    id = models.AutoField(primary_key = True)
    utilisateur = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                help_text='', null =True)
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
    id_number = models.CharField('NIU',max_length=254, unique=True, default ='', null =True)
    hopital = models.ForeignKey( Hopital ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)


    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Medecin_voir", "SATFD: voir"),
                        ("Medecin_voir_inactif", "SATFD: voir inactif"),
                        ("Medecin_voir_details", "SATFD: voir details"),
                        ("Medecin_ajouter", "SATFD: ajouter"),
                        ("Medecin_modifier", "SATFD: modifier"),
                        ("Medecin_activer", "SATFD: activer"),
                        ("Medecin_desactiver", "SATFD: desactiver"),
                        ("Medecin_supprimer", "SATFD: supprimer"),
        )

    def __str__(self):
        return '{0}'.format((self.prenom+' '+self.nom+' '+self.id_number))
class Consulation(models.Model):
    id = models.AutoField(primary_key = True)
    personne_inscrite = models.ForeignKey( Personne ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    medecin = models.ForeignKey( Medecin ,
                                      on_delete=models.SET_NULL,
                                      help_text='',
                                      null = True)
    montant = models.FloatField(null=True)
    date = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,

                              )
    date_created = models.DateField(
                              default=datetime.now, blank=True
                              #null= False,
                              #blank=False
                              )
    created_by = models.CharField(max_length=500, null =True)
    date_modified = models.DateField(null =True)
    modified_by= models.CharField(max_length=500, null =True)
    class Meta:
        ordering = ('date_created',)
        permissions = ( ("Consulation_voir", "SATFD: voir"),
                        ("Consulation_voir_inactif", "SATFD: voir inactif"),
                        ("Consulation_voir_details", "SATFD: voir details"),
                        ("Consulation_ajouter", "SATFD: ajouter"),
                        ("Consulation_modifier", "SATFD: modifier"),
                        ("Consulation_activer", "SATFD: activer"),
                        ("Consulation_desactiver", "SATFD: desactiver"),
                        ("Consulation_supprimer", "SATFD: supprimer"),
        )
    def __str__(self):
        return '{0}'.format("Nom: "+self.personne_inscrite+" Montant: "+self.montant+"Date: "+self.date_created)











################################################################################
