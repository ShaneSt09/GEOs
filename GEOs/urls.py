from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('community-types/', views.getCommunityType),
    path('postcommunitytype/', views.postCommunityType),

    path('parishes/', views.getParish),
    path('postparish/', views.postParish),

    path('communities/', views.getCommunity),
    path('postcommunit/', views.postCommunity),
]