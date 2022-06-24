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
