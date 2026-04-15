# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views
from news import views as news_views

urlpatterns = [
   path('', views.store_view, name='home'), #15.04 Pali - od razu wyświetlanie się strony głównej jako sklep
    path('store/', views.store_view, name='store'),
    path('library/', views.library_view, name='library'),
    path('purchase/<slug:game_slug>/', views.purchase_game, name='purchase_game'),
    path('features/', views.features_page, name='features'), #18.03 Pali- nowe
    path('about', views.about, name='about'),
    path('cars', views.cars, name='cars'),

    path('login', views.login_user, name='login_user'),
    path('register', views.register, name='register_user'),
    path('logout', views.logout_user, name='logout_user'),

    path('request-game/', news_views.request_game, name='request_game'), #18.03 Pali - nowe ścieżki
]
