from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Système Administration"
admin.site.site_title  = "Système Administration"
admin.site.index_title = "Administration"

admin.site.register(Gilet_couleur)
admin.site.register(Lieu_de_travail)
admin.site.register(Personne)
admin.site.register(Surcursale)
admin.site.register(Src_mone_ext)
admin.site.register(Dmd_renfl_ext)
admin.site.register(Dmd_renfl_int)
admin.site.register(Paiements_hebdo)
admin.site.register(Paiements_dettes)
admin.site.register(Prets)
admin.site.register(Morgue)
admin.site.register(Employe_mortuaire)
admin.site.register(Rapport_deces)
admin.site.register(Hopital)
admin.site.register(Medecin)
admin.site.register(Consultation)
