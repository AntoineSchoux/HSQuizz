from django.contrib import admin
from .models import Partie


@admin.register(Partie)
class PartieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nom_du_joueur', 'img', 'img_gold', 'desc_vraie', 'classe_vraie',
                    'desc_fausse1', 'classe_fausse1', 'desc_fausse2', 'classe_fausse2']
    list_editable = ['nom_du_joueur']