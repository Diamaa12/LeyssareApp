from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django import forms

from Leyssare import settings


# Create your models here.

#classe qui s'occupe de crée les membres de notre association
class LeyssareMembres(models.Model):
    nom = models.CharField(max_length=50,null=False)
    prenom = models.CharField(max_length=50, null=False)
    pays = models.CharField(max_length=40, null=False)
    id_number = models.CharField(max_length=10, null=False, blank=True)
    def __str__(self):
        return f"{self.prenom}, {self.nom}, {self.pays}, {self.id_number}"


class VersementLeyssare(models.Model):
    nom = models.CharField(max_length=50, null=False, blank=False)
    prenom = models.CharField(max_length=50, null=False, blank=False)
    pays = models.CharField(max_length=40, null=False)
    montant_cfa = models.FloatField(blank=True, null=True)
    montant_fg = models.FloatField(blank=True, null=True)
    date = models.DateField(auto_now=True)


# Caisse pour les dépenses
class LeyssareDepenses(models.Model):
    nature_de_depense = models.TextField(blank=False)
    montant_depensee = models.FloatField(blank=True, null=True)
    date = models.DateField(auto_now=True)

# Classe de Situation de caisse
class LeyssareCaisse(models.Model):
    montant_cfa_dispo = models.FloatField(null=False, blank=False)
    montant_fg_dispo = models.FloatField(null=False, blank=False)
    montant_depencee = models.FloatField(null=False, blank=False)
    date = models.DateField(auto_now=True)


class VersionPeriodique(models.Model):
    date = models.DateField(auto_now=True)
    #ici, on lie le profil uilisateru crée dans la class VersementLeyssare à la classe VersionPeriodique
    a_versee = models.OneToOneField(VersementLeyssare, on_delete=models.CASCADE)

def connecteur_evenement(sender, instance, created, **kwargs):
    if created:
        VersionPeriodique.objects.create(a_versee=instance)
post_save.connect(connecteur_evenement, sender=VersementLeyssare)

