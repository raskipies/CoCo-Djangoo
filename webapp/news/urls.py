# Plik do zarządzania ścieżkami w aplikacji. Zawiera listę ścieżek powiązanych z widokami.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.news_create, name='news_create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_show'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('bug/<int:bug_id>/delete', views.delete_bug, name='delete_bug'),
    path('comment/<int:comment_id>/delete', views.delete_bug_comment, name='delete_bug_comment'),
]
