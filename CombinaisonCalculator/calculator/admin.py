from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

import calculator.models as models


class PalierAdmin(admin.ModelAdmin):

    list_display = ('id', 'p_numero', 'p_nombre_medailles')
    list_filter = ('id', 'p_numero', 'p_nombre_medailles')


class CaracteristiqueAdmin(admin.ModelAdmin):

    list_display = ('id', 'c_name')
    list_filter = ('id', 'c_name')


class TypeEffetAdmin(admin.ModelAdmin):

    list_display = ('id', 't_name')
    list_filter = ('id', 't_name')


class CouleurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'co_name',
        'co_palier',
        'co_caracteristique',
        'co_effet',
    )
    list_filter = (
        'co_palier',
        'co_caracteristique',
        'id',
        'co_name',
        'co_effet',
    )


class GradeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'g_name',
        'g_type_effet',
        'g_caracteristique',
        'g_effet',
    )
    list_filter = (
        'g_type_effet',
        'g_caracteristique',
        'id',
        'g_name',
        'g_effet',
    )


class ListeMedailleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'l_name',
        'l_color',
        'l_grade',
        'l_bonus',
        'l_malus',
    )
    list_filter = (
        'l_color',
        'l_grade',
        'l_bonus',
        'l_malus',
        'id',
        'l_name',
    )


class CombinaisonAdmin(admin.ModelAdmin):

    list_display = ('id', 'com_name', 'com_effets')
    list_filter = ('id', 'com_name', 'com_effets')
    raw_id_fields = ('com_medailles',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Palier, PalierAdmin)
_register(models.Caracteristique, CaracteristiqueAdmin)
_register(models.TypeEffet, TypeEffetAdmin)
_register(models.Couleur, CouleurAdmin)
_register(models.Grade, GradeAdmin)
_register(models.ListeMedaille, ListeMedailleAdmin)
_register(models.Combinaison, CombinaisonAdmin)
