from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ConnexionAbonne
from .models import Bibliotheque, Abonne, Livre, Emprunt
from datetime import datetime

def index(request):
    return HttpResponse("BUT MMI - Le parcours Dév des gagnants")

def gestionnaire(request):
    return HttpResponse("Administration de la biliothèque")

def abonne(request):
    template = loader.get_template('app1_tb/abonne.html')
    context = {}
    return HttpResponse(template.render(context, request))

def connexionAbonne(request):
    # S'il s'agit d'une requête POST
    if request.method == 'POST':
        # Créer une instance de formulaire
        form = ConnexionAbonne(request.POST)
        # Vérifier si elle est valide
        if form.is_valid():
            idAbonne = 0
            numeroAbonne = form.cleaned_data['numeroAbonne']
            # On récupère son nom et la liste des emprunts

            nomAbonne = Abonne.objects.filter(numero=numeroAbonne).values_list('id', 'nom', 'prenom')
            if nomAbonne.count() > 0:
                idAbonne = nomAbonne[0][0]
            emprunts = Emprunt.objects.select_related('livre__titre').filter(abonne=idAbonne).values_list('livre__titre', 'dateRetour')

            template = loader.get_template('app1_tb/empruntAbonne.html')
            context = {'date_courante': datetime.now, 'nomAbonne': nomAbonne, 'numeroAbonne': numeroAbonne, 'emprunts': emprunts, 'form': form}
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse("Le formulaire n'est pas valide.")