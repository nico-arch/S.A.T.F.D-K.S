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




    ]
