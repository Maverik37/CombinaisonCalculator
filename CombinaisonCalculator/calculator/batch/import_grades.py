#!/bin/env  python3.6

import csv
import os
import sys
import django

#Configuration pour pouvoir importer les modèles django
sys.path.append('/home/fourbasse/scripts/DJANGO/CombinaisonCalculator/CombinaisonCalculator/CombinaisonCalculator/')
os.environ["DJANGO_SETTINGS_MODULE"] = "CombinaisonCalculator.settings"
django.setup()

from calculator.models import *

# Initialisation de certaines variables

file="/home/fourbasse/Téléchargements/grade.csv"

# Définition des fonctions

def is_already_present(color):
    qs_color = Couleur.objects.filter(co_name=color)

    if qs_color.exists():
        return True
    else:
        return False

def get_palier_carac(nb,carac):
    try:
        qs_palier=Palier.objects.filter(p_nombre_medailles=nb)
        qs_caracteristique = Caracteristique.objects.filter(c_name=carac)

        if qs_palier.exists() and qs_caracteristique.exists():
            return qs_palier, qs_caracteristique
    except Exception as e:
        print(e)

def add_color(nb,carac,color,value):
    try:
        obj_color = Couleur()

        #Instance Couleur
        obj_color.co_name = color
        
        # Récupération de l'instance de palier
        obj_palier = Palier.objects.get(p_nombre_medailles=nb)

        #Récupération de l'instance de la couleur
        obj_carac = Caracteristique.objects.get(c_name=carac)
        obj_color.co_palier = obj_palier
        obj_color.co_caracteristique = obj_carac
        obj_color.co_effet = value
        obj_color.save()
    except Exception as e:
        print(e)

#Corps principal du script

with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')

    for row in csvreader:
        color = row[0]
        is_color_present = is_already_present(color)
        if not is_color_present:
            #1er palier
            nb_medaille_first_palier = row[1].split(' ')[0]
            value_first_palier = row[1].split(' ')[2].replace('+','').replace('%','')
            effet_affected_first_palier = row[1].split(' ')[3].replace('_',' ')
            #2eme palier
            nb_medaille_second_palier = row[2].split(' ')[0]
            value_second_palier = row[2].split(' ')[2].replace('+','').replace('%','')
            effet_affected_second_palier = row[2].split(' ')[3].replace('_',' ')
            #3eme palier
            nb_medaille_third_palier = row[2].split(' ')[0]
            value_third_palier = row[2].split(' ')[2].replace('+','').replace('%','')
            effet_affected_third_palier = row[2].split(' ')[3].replace('_',' ')

            #Ajout en base
            try:
                add_color(nb_medaille_first_palier,effet_affected_first_palier,color,value_first_palier)
                add_color(nb_medaille_second_palier,effet_affected_second_palier,color,value_second_palier)
                add_color(nb_medaille_third_palier,effet_affected_third_palier,color,value_third_palier)
            except Exception as e:
                print(e)
          
