from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Système Administration"
admin.site.site_title  = "Système Administration"
admin.site.index_title = "Administration"

admin.site.register(Lieu_de_travail)
admin.site.register(Personne)



