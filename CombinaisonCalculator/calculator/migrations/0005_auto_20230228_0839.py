# Generated by Django 3.2.15 on 2023-02-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_grade_g_effet'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='g_is_percentage',
            field=models.BooleanField(default=False, verbose_name='Pourcentage'),
        ),
        migrations.AlterField(
            model_name='couleur',
            name='co_effet',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Valeur(%)'),
        ),
    ]
