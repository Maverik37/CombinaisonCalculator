from django.db import models

class Palier(models.Model):
    p_numero = models.IntegerField(verbose_name="Numeros")
    p_nombre_medailles = models.IntegerField(verbose_name="Nombre de médailles")

    def __str__(self):
        return str(self.p_numero)+"_"+str(self.p_nombre_medailles)

class Caracteristique(models.Model):
    c_name = models.CharField(max_length=100 , verbose_name="Nom")

    def __str__(self):
        return self.c_name
    
class TypeEffet(models.Model):
    t_name = models.CharField(max_length=10, verbose_name="Type")

    def __str__(self):
        return self.t_name
    
class Couleur(models.Model):
    co_name = models.CharField(max_length=100 , verbose_name="Couleur")
    co_palier = models.ForeignKey(Palier,on_delete=models.CASCADE , related_name="p_couleur", verbose_name="Palier", blank=True, null=True)
    co_caracteristique = models.ForeignKey(Caracteristique, on_delete=models.CASCADE , related_name="co_caracteristique_name", verbose_name="Caractéristiques",blank=True,null=True)
    co_effet = models.DecimalField(verbose_name="Valeur(%)", max_digits=3 , decimal_places=2)

class Grade(models.Model):
    g_name = models.CharField(max_length=50 , verbose_name="Nom")
    g_type_effet = models.ForeignKey(TypeEffet, on_delete=models.CASCADE, related_name="t_grade_type_effet", verbose_name="Type")
    g_caracteristique = models.ForeignKey(Caracteristique, on_delete=models.CASCADE , related_name="g_caracteristique", verbose_name="Caractéristiques",blank=True,null=True)
    g_effet = models.DecimalField(verbose_name="Valeur effet",max_digits=3 , decimal_places=1)
    g_is_percentage = models.BooleanField(default=False,verbose_name="Pourcentage")

    def __str__(self):
        return self.g_name+"_"+self.g_type_effet.t_name+"_"+self.g_caracteristique.c_name

class ListeMedaille(models.Model):
    l_name = models.CharField(max_length=200, verbose_name="Nom")
    l_color = models.ForeignKey(Couleur, on_delete=models.CASCADE, related_name="co_liste_medaille", verbose_name="Couleur")
    l_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="l_grade_effect",verbose_name="Grade",blank=True, null= True)
    l_bonus = models.ForeignKey(Caracteristique, on_delete=models.CASCADE, related_name="c_bonus",verbose_name="BONUS",blank=True, null= True)
    l_malus = models.ForeignKey(Caracteristique, on_delete=models.CASCADE, related_name="c_malus",verbose_name="MALUS",blank=True, null= True)

    def __str__(self):
        return self.l_name+"_"+self.l_color.co_name+"_"+self.l_grade.g_name
    
class Combinaison(models.Model):
    com_name = models.CharField(max_length=200, verbose_name="Nom")
    com_medailles = models.ManyToManyField(ListeMedaille, related_name="com_liste_medailles",verbose_name="Médailles")
    com_effets = models.TextField(max_length=500, verbose_name="Résultat")

    def __str__(self):
        return self.com_name

