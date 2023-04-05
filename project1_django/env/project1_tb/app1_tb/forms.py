from django import forms

class ConnexionAbonne (forms.Form): # Nom du formulaire
    numeroAbonne = forms.CharField(max_length=10)