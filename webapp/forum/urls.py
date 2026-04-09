from django.urls import path
from . import views # from current folder import the neighbour file views for views methods usage

urlpatterns = [
    path('', views.index, name='forum_index'),
    path('delete/<int:post_id>/', views.delete_post, name='forum_delete_post'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='forum_delete_comment'),
    path('frequent_questions', views.frequent_questions)
]
 