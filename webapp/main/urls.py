# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views
from news import views as news_views

urlpatterns = [
    path('', views.index, name='home'),
    path('features/', views.features_page, name='features'), #18.03 Pali- nowe
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),

    path('login', views.login_user, name='login_user'),
    path('register', views.register, name='register_user'),
    path('logout', views.logout_user, name='logout_user'),

    path('request-game/', news_views.request_game, name='request_game'), #18.03 Pali - nowe ścieżki
]
