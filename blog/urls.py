from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('update-article/<int:pk>', views.update_article, name='update-article'),
    path('delete-article/<int:pk>', views.delete_article, name='delete-article'),


    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
