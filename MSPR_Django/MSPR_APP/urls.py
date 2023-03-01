from django.urls import path
from MSPR_APP import views

urlpatterns = [
    path('Accueil',views.index,name="Accueil"),
    path('connexion',views.connexion,name='connexion'),
    path('inscription',views.inscription,name='inscription'),
    path('outil',views.outil,name='outil'),
    path('',views.index,name='index'),
    path('index_log',views.index_log,name='index_log'),
    path('messagerie',views.messagerie,name='messagerie'),
    path('outil_log',views.outil_log,name='outil_log'),
    path('profile',views.profile,name='profile')
]