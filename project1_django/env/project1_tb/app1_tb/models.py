from django.db import models

# Create your models here.
class Bibliotheque (models.Model):
    nom = models.CharField(default=None, max_length=50)
    ville = models.CharField(default=None, max_length=50)

    def __str__(self):
        # Utilisé par les filtres des requêtes SELECT
        return self.nom

class Abonne (models.Model):
    numero = models.CharField(default=None, max_length=10)
    nom = models.CharField(default=None, max_length=50)
    prenom = models.CharField(default=None, max_length=50)
    courriel = models.CharField(default=None, max_length=150)
    bibliotheque = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE)

    def __str__(self):
        # Utilisé par les filtres des requêtes SELECT
        return self.nom + ' ' + self.prenom

class Livre (models.Model):
    ISBN = models.CharField(default=None, max_length=50)
    titre = models.CharField(default=None, max_length=150)
    editeur = models.CharField(default=None, max_length=50)
    bibliotheque = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE)

    def __str__(self):
        # Utilisé par les filtres des requêtes SELECT
        return self.titre

class Emprunt (models.Model):
    dateEmprunt = models.DateTimeField()
    dateRetour = models.DateTimeField()
    abonne = models.ForeignKey(Abonne, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    def __str__(self):
        # Utilisé par les filtres des requêtes SELECT
        return self.livre.titre + ' - ' + self.livre.editeur + ' - du ' + self.dateEmprunt.strftime(("%d.%m.%Y %H:%M")) + ' au ' + self.dateRetour.strftime(("%d.%m.%Y %H:%M"))