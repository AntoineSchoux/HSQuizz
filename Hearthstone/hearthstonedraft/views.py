from django.shortcuts import render_to_response
from .models import Partie

def home(request):
    partie = Partie.objects.get_or_create(nom_du_joueur = 'Hearlcash')[0]
    return render_to_response('hearth.html', {
    'partie': partie }
    )

