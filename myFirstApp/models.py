from django.db import models

class Etudiant(models.Model):
  prenom= models.CharField(max_length=255)
  nom= models.CharField(max_length=255)
  # age= models.IntegerField()
  email= models.EmailField(max_length=255,null=True)
  # password= models.CharField(max_length=255)
  matricule= models.CharField(max_length=255, null=True)
  telephone= models.IntegerField(null=True)
  # date_naissance= models.DateField(_("Date de Naissance"), auto_now=False, auto_now_add=False)