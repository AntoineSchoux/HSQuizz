from django.db import models
import random
import requests
from django.utils.html import mark_safe
from django.utils.functional import cached_property
import requests_cache
import re

requests_cache.install_cache()
r = requests.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards?locale=frFR",
                 headers={"X-Mashape-Key": "ScpmlSTQx6msh8Q3S5TiqanAFaXKp1u7lkAjsncmwi0zNJB2c4"})
extensions = ['Basic', 'Classic', "Journey to Un'Goro", 'Knights of the Frozen Throne', 'Kobolds & Catacombs', 'The Witchwood', 'The Boomsday Project', 'Goblins vs Gnomes', 'The Grand Tournament', 'Whispers of the Old Gods', 'Mean Streets of Gadgetzan', 'Hall of Fame']

liste = r.json()[(random.choice(extensions))]


class Partie(models.Model):
    nom_du_joueur = models.CharField(max_length=50)

    def __str__(self):
        return f'Partie n° {self.id}'

    @cached_property
    def carte_vraie(self):
        while True:
            choix = random.choice(liste)
            if 'imgGold' in choix and 'img' in choix and 'text' in choix:
                return choix

    def img(self):
        url_old = self.carte_vraie['img']
        url_old = url_old[61:]
        url = 'https://media.services.zam.com/v1/media/byName/hs/cards/enus/'
        return mark_safe(f"<img src='{url + url_old}'/>")

    def img_gold(self):
        return mark_safe(f"<img src='{self.carte_vraie['imgGold']}'/>")

    def desc_vraie(self):
        text = self.carte_vraie['text']
        return re.sub('\W', ' ', text)

    def classe_vraie(self):
        return self.carte_vraie['playerClass']

    def nom_vraie(self):
        return self.carte_vraie['name']

    @cached_property
    def carte_fausse1(self):
        while True:
            choix = random.choice(liste)
            if 'text' in choix and choix['playerClass'] != self.carte_vraie['playerClass'] and choix[
                'playerClass'] != 'Death Knight':
                return choix

    def desc_fausse1(self):
        text = self.carte_fausse1['text']
        return re.sub('\W', ' ', text)

    def classe_fausse1(self):
        return self.carte_fausse1['playerClass']

    @cached_property
    def carte_fausse2(self):
        while True:
            choix = random.choice(liste)
            if 'text' in choix and choix['playerClass'] != self.carte_vraie['playerClass'] and choix[
                'playerClass'] != 'Death Knight':
                return choix

    def desc_fausse2(self):
        text = self.carte_fausse2['text']
        return re.sub('\W', ' ', text)

    def classe_fausse2(self):
        return self.carte_fausse2['playerClass']