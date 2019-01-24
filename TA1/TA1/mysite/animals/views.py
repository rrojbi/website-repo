from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Animal, Action
from django.urls import reverse
from django.views import generic
import json

animal_data = 'animal.json'
équipement_data = 'equipement.json'



def index(request):
    animals_list = Animal.objects.all()
    actions_list = Action.objects.all()
    return render(request, 'animals/index.html',{'animals_list':animals_list,'actions_list':actions_list})


def results(request,animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, 'animals/results.html', {'animal': animal})

def vote(request):
    actions_list = Action.objects.all()
    animals_list = Animal.objects.all()
    try:
        selected_animal0 = animals_list.id_animal=request.POST['a']
        selected_action0= Action.objects.Action_text=request.POST['b']
        selected_animal= animals_list.get(pk=selected_animal0)
        selected_action = actions_list.get(pk=selected_action0)


    except ((KeyError,Action.DoesNotExist) or (KeyError,Animal.DoesNotExist)):
        # Redisplay the question voting form.
        return render(request, 'animals/index.html', {'animals_list':animals_list,'actions_list':actions_list,'error_message': "Il vous manque un choix.",
        })


    else:
        if selected_action.Action_text=="nourrir" :

            etat=selected_animal.Etat
            lieu=selected_animal.Lieu

            with open(équipement_data, "r") as f:
                equipement = json.load(f)
            if equipement["mangeoire"]["DISPONIBILITÉ"]=="libre":
                dispo=1
            else:
                dispo=0
            if etat != 'affamé':

                print('Désolé,', selected_animal.id_animal, "n'a pas faim...")
            else :
                if dispo==0:

                    print('Désolé, la mangeoire est occupée')
                else:
                    selected_animal.Etat="repus"

                    lieu_vacant = selected_animal.Lieu
                    equipement["mangeoire"]['DISPONIBILITÉ'] = 'occupé'
                    equipement[lieu_vacant]['DISPONIBILITÉ'] = 'libre'
                    selected_animal.Lieu="mangeoire"
                    selected_animal.save()
            with open(équipement_data, "w") as g2:
                json.dump(equipement, g2)

        if selected_action.Action_text=="divertir" :

            etat=selected_animal.Etat
            lieu=selected_animal.Lieu

            with open(équipement_data, "r") as f:
                equipement = json.load(f)
            if equipement["roue"]["DISPONIBILITÉ"]=="libre":
                dispo=1
            else:
                dispo=0
            if etat != 'repus':

                print('Désolé,', selected_animal.id_animal, "n'est pas en état de faire du sport")
            else :
                if dispo==0:

                    print('Désolé, la roue est occupée')
                else:
                    selected_animal.Etat="fatigué"

                    lieu_vacant = selected_animal.Lieu
                    equipement["roue"]['DISPONIBILITÉ'] = 'occupé'
                    equipement[lieu_vacant]['DISPONIBILITÉ'] = 'libre'
                    selected_animal.Lieu="roue"
                    selected_animal.save()
            with open(équipement_data, "w") as g2:
                json.dump(equipement, g2)

        if selected_action.Action_text=="coucher" :

            etat=selected_animal.Etat
            lieu=selected_animal.Lieu

            with open(équipement_data, "r") as f:
                equipement = json.load(f)
            if equipement["nid"]["DISPONIBILITÉ"]=="libre":
                dispo=1
            else:
                dispo=0
            if etat != 'fatigué':

                print('Désolé,', selected_animal.id_animal, "n'a pas envie de dormir")
            else :
                if dispo==0:

                    print('Désolé, le nid est occupé')
                else:
                    selected_animal.Etat="endormi"

                    lieu_vacant = selected_animal.Lieu
                    equipement["nid"]['DISPONIBILITÉ'] = 'occupé'
                    equipement[lieu_vacant]['DISPONIBILITÉ'] = 'libre'
                    selected_animal.Lieu="nid"
                    selected_animal.save()
            with open(équipement_data, "w") as g2:
                json.dump(equipement, g2)

        if selected_action.Action_text=="réveiller" :

            etat=selected_animal.Etat
            lieu=selected_animal.Lieu

            with open(équipement_data, "r") as f:
                equipement = json.load(f)
            if equipement["litière"]["DISPONIBILITÉ"]=="libre":
                dispo=1
            else:
                dispo=0
            if etat != 'endormi':

                print('Désolé,', selected_animal.id_animal, "n'est pas endormi")
            else :
                if dispo==0:

                    print('Désolé, la litière est occupée')
                else:
                    selected_animal.Etat="affamé"

                    lieu_vacant = selected_animal.Lieu
                    equipement[lieu_vacant]['DISPONIBILITÉ'] = 'libre'
                    selected_animal.Lieu="litière"
                    selected_animal.save()
            with open(équipement_data, "w") as g2:
                json.dump(equipement, g2)






        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('animals:results',args=(selected_animal.id,)))

