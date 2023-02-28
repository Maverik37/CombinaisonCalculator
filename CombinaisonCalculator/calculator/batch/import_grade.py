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

file="/home/fourbasse/Téléchargements/grades.csv"

#Définitions des fonctions

def is_grade_present(name,type):
    obj_grade = Grade.objects.filter(g_name=name,g_type_effet=type)

    if obj_grade.exists():
        is_present=True
    else:
        is_present=False
    
    return is_present

#Corps principal

dict_grade = {}

with open(file,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')
    header = next(csvreader)

    print(header)
    for row in csvreader:
        dict_grade[row[0]]={}
        first_grade = 

