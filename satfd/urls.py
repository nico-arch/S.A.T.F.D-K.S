from django.conf.urls import url
from django.urls import path, include
from . import views
# from .views_path.homepage import home_views


urlpatterns = [
  path('', views.dashboard, name='index'),
#Front-End home page
    path('', views.dashboard, name='dashboard-index'),
#Dashboard login page
    path('login/', views.dashboard_login, name='dashboard-login'),
#Dashboard logout page
    path('logout/', views.dashboard_logout, name='dashboard-logout'),
#Dashboard home page
    path('dashboard/change_password', views.dashboard_change_password, name='dashboard-change-password'),
#Dashboard access-denied page
    path('dashboard/access-denied', views.error_403, name='dashboard-access-denied'),

#Section CRUD Personne

    #Afficher
    path('dashboard/satfd/personne/afficher', views.dashboard_satfd_personne_afficher, name='dashboard-satfd-personne-afficher'),
    #Ajouter
    path('dashboard/satfd/personne/ajouter', views.dashboard_satfd_personne_ajouter, name='dashboard-satfd-personne-ajouter'),
    #Modifier
    path('dashboard/satfd/personne/modifier/<int:personne_pk>', views.dashboard_satfd_personne_modifier, name='dashboard-satfd-personne-modifier'),
    #Afficher
    path('dashboard/satfd/personne/afficher_details/<int:personne_pk>', views.dashboard_satfd_personne_afficher_details, name='dashboard-satfd-personne-afficher-details'),
    #Supprimer
    path('dashboard/satfd/personne/suprimer/<int:personne_pk>/', views.dashboard_satfd_personne_suprimer, name='dashboard-satfd-personne-suprimer'),



    ]
