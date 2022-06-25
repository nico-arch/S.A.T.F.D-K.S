from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from datetime import datetime
import json
from .models import *
from .forms import *
from .custom_decorators import *
from .mail_sender import *
# Create your views here.



def dashboard_login(request):
    data = {
            'username': request.POST.get("username",""),
            'password': request.POST.get("password",""),
            }

    if request.user.is_authenticated:

        if request.user.is_staff == False:
            logout(request)
            messages.error(request, f'Votre compte a été desactivé.')
            return render(request, 'dashboard/login.html')

        # send_email( 'Test subject', 'Test message', ['newnick1996@gmail.com', 'azemarand@gmail.com'])
        # send_email_to_group( 'Test subject 2', 'Test message 2', 1)
        return redirect('dashboard-index')
    else:
        #si l'utilisateur appuis sur s'authenfier
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if  username == "": # return True/False
                #Envoyer un message d'erreur et reste data la page actuelle
                messages.error(request, f'Veuiller remplir tous les champs.')
                return render(request, 'satfd/dashboard/login.html')

            if  password == "": # return True/False
                #Envoyer un message d'erreur et reste data la page actuelle
                messages.error(request, f'Veuiller remplir tous les champs.')
                return render(request, 'satfd/dashboard/login.html')


            user = authenticate(request, username= str(username), password= str(password) )
            if user is not None:
                # A backend authenticated the credentials
                #messages.success(request, f"Le Type {request.POST.get('libelle','')} a été modifier avec succès")
                login(request, user)
                return redirect('dashboard-index')




            else:
                # No backend authenticated the credentials
                #Wait for authentification...
                messages.success(request, f"Le nom d'utilisateur/mot de passe n'existe pas sur le système.")
                return render(request, 'satfd/dashboard/login.html')
    return render(request, 'satfd/dashboard/login.html')

@custom_login_required()
def dashboard_logout(request):
    if request.method == 'POST':
        logout(request)
        #Envoyer un message de succès et se redirectionne a la page d'affichage
        messages.success(request, f"Déconnecter avec succès.")
        return redirect('dashboard-login')

    return render(request, 'satfd/dashboard/logout.html')

#Afficher la page d'acceuil du tableau de bord
@custom_login_required()
def dashboard(request):
    user = User.objects.get(pk = request.user.pk)

    if request.user.is_superuser:
        data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_dgc': 0,
                }

        return render(request, 'satfd/dashboard/index.html', data)


    else:
        data = {
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_dgc': 1, #user est un dgc
                }





    return render(request, 'satfd/dashboard/index.html', data)
    # return render(request, 'dashboard/index.html')


#Afficher la page d'acceuil du tableau de bord
#def dashboard_access_denied(request):
#    return render(request, 'dashboard/access_denied.html')
@custom_login_required()
def error_403(request, exception):
    return render(request,'satfd/dashboard/403.html')

@custom_login_required()
def dashboard_change_password(request):

    if request.method == 'POST':
        #Quelques tests
        #Tester le type d'absences
        if request.POST.get("password","") == "" or request.POST.get("newpassword","") == "":
            messages.error(request, f'Veuiller remplir tous les champs.')
            return render(request, 'satfd/dashboard/change_password.html')

        if request.POST.get("password","") != request.POST.get("newpassword",""):
            messages.error(request, f'Vous aviez tapé deux mots de passe différents.')
            return render(request, 'satfd/dashboard/change_password.html')

        if len(request.POST.get("password","")) < 8  or len(request.POST.get("newpassword","")) < 8:
            messages.error(request, f'Le mot de passe doit comporter au moins 8 caractères.')
            return render(request, 'satfd/dashboard/change_password.html')

        if request.POST.get("password","") == request.POST.get("newpassword","") and int(len(request.POST.get("newpassword","")) >= 8):
            #change le mot de passe de l'utilisateur
            newpassword = request.POST.get("newpassword", "")
            actual_user = request.user
            actual_user.set_password(newpassword)
            actual_user.save()
            logout(request)
            #Envoyer un message de succès et se redirectionne a la page d'affichage
            messages.success(request, f"Mot de passe changé avec succès.")
            return redirect('dashboard-login')

    return render(request,'satfd/dashboard/change_password.html')

#Section des Personne###########################################################
#Afficher
@custom_login_required()
@check_permisions('satfd.Personne_voir')
def dashboard_satfd_personne_afficher(request):
    #Rechercher tous les references
    output = Personne.objects.all().order_by('-date_created')

    context = {
        #'users': users,
        'output': output,
        'header':f"Liste des personnes adultes inscrites, quantité: {output.count()}",
        'title': f'Liste des personnes adultes inscrites, quantité: {output.count()}',
        'boutton_ajouter': "Inscrire une personne adulte",
        }

    return render(request, 'satfd/dashboard/registre/personne/afficher.html', context)



#Ajouter
@custom_login_required()
@check_permisions('satfd.Personne_ajouter')
def dashboard_satfd_personne_ajouter(request):
  #Si l'utilisateur apuis sur le boutton ajouter
  if request.method == 'POST':
      form = PersonneForm(request.POST)



      #data = {'form':form,}
      #Si le formulaire transmis au system est valide
      request.POST._mutable = True
      request.POST['date_created'] = f"{datetime.now().strftime('%Y-%m-%d')}"
      request.POST['created_by'] = f"{request.user.username}"
      # request.POST['statut'] = "En cours"
      # request.POST['date_modified'] = "-"
      # request.POST['modified_by'] = "-"


      if form.is_valid():
          #Si le NUI du/de la conjoint(e) n'existe pas return une alerte
          if len(str(form.cleaned_data['conjoint'])) == 10: #Si l'input n'est pas vide
              if not Personne.objects.filter(id_number = form.cleaned_data['conjoint']).exists():

                  data = {
                  'form':form,
                  'header':"Inscrire une personne",
                  'title': f'Inscrire une personne',}
                  messages.success(request, f"Conjoint(e): Aucune personne ayant ce NIU: {form.cleaned_data['conjoint']} existe dans le registe")
                  return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)


          #Si le NUI du père n'existe pas returne une alerte
          if  len(str(form.cleaned_data['pere_cin_nif'])) == 10: #Si l'input n'est pas vide
              if not Personne.objects.filter(id_number = form.cleaned_data['pere_cin_nif']).exists():

                  data = {
                  'form':form,
                  'header':"Inscrire une personne adulte",
                  'title': f'Inscrire une personne adulte',}
                  messages.success(request, f"Père: Aucune personne ayant ce NIU: {form.cleaned_data['pere_cin_nif']} existe dans le registe")
                  return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)

          #Si le NUI de la mère n'existe pas returne une alerte
          if len(str(form.cleaned_data['mere_cin_nif'])) == 10: #Si l'input n'est pas vide
              if not Personne.objects.filter(id_number = form.cleaned_data['mere_cin_nif']).exists():

                  data = {
                  'form':form,
                  'header':"Inscrire une personne",
                  'title': f'Inscrire une personne',}
                  messages.success(request, f"Mère: Aucune personne ayant ce NIU: {form.cleaned_data['mere_cin_nif']} existe dans le registe")
                  return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)
          form.save()
          #Envoyer un message de succès et se redirectionne a la page d'affichage
          messages.success(request, f"{form.cleaned_data['prenom']} {form.cleaned_data['nom']} a été inscrit avec succès")
          # send_email_to_group( '', '', 2)
          return redirect('dashboard-satfd-personne-afficher')

      #Si le formulaire transmit au system n'est pas valide
      else:
          form = PersonneForm(request.POST)
          data = {
          'form':form,
          'header':"Inscrire une personne adulte",
          'title': f'Inscrire une personne adulte',}
          return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)

  return render(request, 'satfd/dashboard/registre/personne/ajouter.html',{'form':PersonneForm(),'header':"Inscrire une personne", 'title': f'Inscrire une personne',} )


#Modifier
@custom_login_required()
@check_permisions('satfd.Personne_modifier')
def dashboard_satfd_personne_modifier(request, personne_pk):
    item = Personne.objects.get(id = personne_pk)
    if request.method == 'POST':
        form = PersonneForm(request.POST, instance=item)
        request.POST._mutable = True
        request.POST['date_modified'] = f"{datetime.now().strftime('%Y-%m-%d')}"
        request.POST['modified_by'] = str(request.user.username)

        if form.is_valid():
            #Si le NUI du/de la conjoint(e) n'existe pas return une alerte
            if len(str(form.cleaned_data['conjoint'])) == 10: #Si l'input n'est pas vide
                if not Personne.objects.filter(id_number = form.cleaned_data['conjoint']).exists():

                    data = {
                    'form':form,
                    'header':"Inscrire une personne adulte",
                    'title': f'Inscrire une personne adulte',}
                    messages.success(request, f"Conjoint(e): Aucune personne ayant ce NIU: {form.cleaned_data['conjoint']} existe dans le registe")
                    return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)


            #Si le NUI du père n'existe pas returne une alerte
            if  len(str(form.cleaned_data['pere_cin_nif'])) == 10: #Si l'input n'est pas vide
                if not Personne.objects.filter(id_number = form.cleaned_data['pere_cin_nif']).exists():

                    data = {
                    'form':form,
                    'header':"Inscrire une personne adulte",
                    'title': f'Inscrire une personne adulte',}
                    messages.success(request, f"Père: Aucune personne ayant ce NIU: {form.cleaned_data['pere_cin_nif']} existe dans le registe")
                    return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)

            #Si le NUI de la mère n'existe pas returne une alerte
            if len(str(form.cleaned_data['mere_cin_nif'])) == 10: #Si l'input n'est pas vide
                if not Personne.objects.filter(id_number = form.cleaned_data['mere_cin_nif']).exists():

                    data = {
                    'form':form,
                    'header':"Inscrire une personne adulte",
                    'title': f'Inscrire une personne adulte',}
                    messages.success(request, f"Mère: Aucune personne ayant ce NIU: {form.cleaned_data['mere_cin_nif']} existe dans le registe")
                    return render(request, 'satfd/dashboard/registre/personne/ajouter.html', data)
            form.save()
            #Envoyer un message de succès et se redirectionne a la page d'affichage
            messages.success(request, f"{form.cleaned_data['prenom']} {form.cleaned_data['nom']} a été modifier avec succès")
            return redirect('dashboard-satfd-personne-afficher')
        else:
            form = PersonneForm(request.POST)
            data = {
            'form':form,
            'header':"Modifier une personne adulte",
            'title': f'Modifier une personne adulte:',
            }
            return render(request, 'satfd/dashboard/registre/personne/modifier.html', data)
    else:
        form = PersonneForm(instance=item)
    context = {
        'form': form,
        'header':"Modifier une personne adulte",
        'title': f'Modifier une personne adulte:',
    }
    return render(request, 'satfd/dashboard/registre/personne/modifier.html', context)


#Afficher les details
@custom_login_required()
@check_permisions('satfd.Personne_voir_details')
def dashboard_satfd_personne_afficher_details(request, personne_pk):
    output = Personne.objects.get(pk = personne_pk)
    form =  PersonneForm(request.POST, instance = output, initial={'gilet_couleur':output.gilet_couleur,
                                                                  'lieu_de_travail':output.lieu_de_travail,
                                                                  'sexe':output.sexe})
    form.fields['naissance'].required = True
    form.fields['email'].required = True
    form.fields['lieu_de_travail'].required = True
    form.fields['id_plaque'].required = True
    form.fields['gilet_couleur'].required = True
    form.fields['conjoint'].required = True
    form.fields['pere_cin_nif'].required = True
    form.fields['mere_cin_nif'].required = True
    
    
    form.fields['telephone'].label = "Téléphone"    
    form.fields['id_number'].label = "NIU"
    form.fields['conjoint'].label = "NIU du/de la conjoint(e)"
    form.fields['pere_cin_nif'].label = "NIU du père"
    form.fields['mere_cin_nif'].label = "NIU de la mère"

    data = {
            'output': output,
            'header': "Personne details",
            'title': f'{output.prenom} {output.nom}: NIU = { output.id_number }',

            'form':form,
            }
    return render(request, 'satfd/dashboard/registre/personne/afficher_details.html', data)



#Supprimer
@custom_login_required()
@check_permisions('satfd.Personne_supprimer')
def dashboard_satfd_personne_suprimer(request, personne_pk ):
    output = Personne.objects.get(pk = personne_pk)
    form = PersonneForm(request.POST, instance = output, initial={'gilet_couleur':output.gilet_couleur,
                                                                  'lieu_de_travail':output.lieu_de_travail,
                                                                  'sexe':output.sexe})
    form.fields['naissance'].required = True
    form.fields['email'].required = True
    form.fields['lieu_de_travail'].required = True
    form.fields['id_plaque'].required = True
    form.fields['gilet_couleur'].required = True
    form.fields['conjoint'].required = True
    form.fields['pere_cin_nif'].required = True
    form.fields['mere_cin_nif'].required = True

    data = {
            'output': output,
            'header': "Supprimer une Personne adulte",
            'title': f'Voulez-vous supprimer {output.prenom} {output.nom}: NIU = {output.id_number} ?',
            'form': form,
            }

    if request.method == 'POST':
        output.delete()
        #Envoyer un message de succès et se redirectionne a la page d'affichage
        messages.success(request, f"{output.prenom} {output.nom}: NIU = {output.id_number} a été supprimer avec succès")
        return redirect('dashboard-satfd-personne-afficher')

    return render(request, 'satfd/dashboard/registre/personne/supprimer.html', data)
