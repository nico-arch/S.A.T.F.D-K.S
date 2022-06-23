from django.conf.urls import url
from django.urls import path, include
from . import views
# from .views_path.homepage import home_views


urlpatterns = [
#Front-End home page
    path('', views.dashboard, name='dashboard-index'),
#Dashboard login page
    path('login/', views.dashboard_login, name='dashboard-login'),
#Dashboard logout page
    path('logout/', views.dashboard_logout, name='dashboard-logout'),





    ]
